def _get(self, url, params={}):
    req = self._session.get(self._api_prefix + url, params=params)
    return self._action(req)