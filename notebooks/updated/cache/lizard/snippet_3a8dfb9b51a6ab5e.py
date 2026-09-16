def upsert(self, body, raise_exc=True, headers=False, files=None):
    return self._request(PUT, body, raise_exc, headers, files)