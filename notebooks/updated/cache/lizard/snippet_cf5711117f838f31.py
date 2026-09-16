def _do_refresh_request(self, unused_http_request):
    relative_url = 'instance/service-accounts/{0}/token'.format(self.
        __service_account_name)
    try:
        response = _GceMetadataRequest(relative_url)
    except exceptions.CommunicationError:
        self.invalid = True
        if self.store:
            self.store.locked_put(self)
        raise
    content = response.read()
    try:
        credential_info = json.loads(content)
    except ValueError:
        raise exceptions.CredentialsError(
            'Could not parse response as JSON: %s' % content)
    self.access_token = credential_info['access_token']
    if 'expires_in' in credential_info:
        expires_in = int(credential_info['expires_in'])
        self.token_expiry = datetime.timedelta(seconds=expires_in
            ) + datetime.datetime.utcnow()
    else:
        self.token_expiry = None
    self.invalid = False
    if self.store:
        self.store.locked_put(self)