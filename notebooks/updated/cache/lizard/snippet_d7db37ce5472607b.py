def _http_get(self, url, query, **kwargs):
    self._normalize_query(query)
    kwargs.update({'params': query})
    return self._http_request('get', url, kwargs)