def adjust_uri(self, uri, relativeto):
    key = uri, relativeto
    if key in self._uri_cache:
        return self._uri_cache[key]
    if uri[0] != '/':
        if relativeto is not None:
            v = self._uri_cache[key] = posixpath.join(posixpath.dirname(
                relativeto), uri)
        else:
            v = self._uri_cache[key] = '/' + uri
    else:
        v = self._uri_cache[key] = uri
    return v