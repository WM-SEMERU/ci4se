def auth(username, password):
    _cred = __get_yubico_users(username)
    client = Yubico(_cred['id'], _cred['key'])
    try:
        return client.verify(password)
    except yubico_exceptions.StatusCodeError as e:
        log.info('Unable to verify YubiKey `%s`', e)
        return False