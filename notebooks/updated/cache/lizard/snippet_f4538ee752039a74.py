def _get_request(self, url, headers, params=None):
    return self._session.get(url, headers=headers, params=params)