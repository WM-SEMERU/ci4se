def origin(self):
    if not self.is_absolute():
        raise ValueError('URL should be absolute')
    if not self._val.scheme:
        raise ValueError('URL should have scheme')
    v = self._val
    netloc = self._make_netloc(None, None, v.hostname, v.port, encode=False)
    val = v._replace(netloc=netloc, path='', query='', fragment='')
    return URL(val, encoded=True)