def authenticate(self, api_key):
    self._api_key = api_key
    self._session.auth = '', self._api_key
    return self._verify_api_key()