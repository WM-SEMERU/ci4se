def search(self, q=''):
    if q:
        q = '?q=' + q
    return self._http_call('/v1/search' + q, get)