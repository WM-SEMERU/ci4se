def login(self, username, password='', login_key=None, auth_code=None,
    two_factor_code=None, login_id=None):
    self._LOG.debug('Attempting login')
    if not self._pre_login():
        return EResult.TryAnotherCM
    self.username = username
    message = MsgProto(EMsg.ClientLogon)
    message.header.steamid = SteamID(type='Individual', universe='Public')
    message.body.protocol_version = 65579
    message.body.client_package_version = 1771
    message.body.client_os_type = EOSType.Windows10
    message.body.client_language = 'english'
    message.body.should_remember_password = True
    message.body.supports_rate_limit_response = True
    if login_id is None:
        message.body.obfustucated_private_ip = ip_to_int(self.connection.
            local_address) ^ 4027431597
    else:
        message.body.obfustucated_private_ip = login_id
    message.body.account_name = username
    if login_key:
        message.body.login_key = login_key
    else:
        message.body.password = password
    sentry = self.get_sentry(username)
    if sentry is None:
        message.body.eresult_sentryfile = EResult.FileNotFound
    else:
        message.body.eresult_sentryfile = EResult.OK
        message.body.sha_sentryfile = sha1_hash(sentry)
    if auth_code:
        message.body.auth_code = auth_code
    if two_factor_code:
        message.body.two_factor_code = two_factor_code
    self.send(message)
    resp = self.wait_msg(EMsg.ClientLogOnResponse, timeout=30)
    if resp and resp.body.eresult == EResult.OK:
        self.sleep(0.5)
    return EResult(resp.body.eresult) if resp else EResult.Fail