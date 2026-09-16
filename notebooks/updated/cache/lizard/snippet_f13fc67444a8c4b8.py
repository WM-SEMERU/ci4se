def _headers(self, **kwargs):
    headers = BASE_HEADERS.copy()
    if self._token:
        headers['X-Plex-Token'] = self._token
    headers.update(kwargs)
    return headers