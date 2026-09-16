def replace(self, key, value, expire=0, noreply=None):
    if noreply is None:
        noreply = self.default_noreply
    return self._store_cmd(b'replace', {key: value}, expire, noreply)[key]