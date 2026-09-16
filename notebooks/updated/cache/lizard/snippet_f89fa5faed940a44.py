def getall(self, key, default=_marker):
    identity = self._title(key)
    res = [v for i, k, v in self._impl._items if i == identity]
    if res:
        return res
    if not res and default is not _marker:
        return default
    raise KeyError('Key not found: %r' % key)