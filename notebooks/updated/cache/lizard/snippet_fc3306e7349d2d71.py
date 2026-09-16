def set_auth_credentials(username, password):
    global _credentials, _dirty
    LOGGER.debug('Setting authentication credentials')
    _credentials = username, password
    _dirty = True