def contains(self, key):
    if self._jconf is not None:
        return self._jconf.contains(key)
    else:
        return key in self._conf