def deregister(self, key):
    if not key in self._actions:
        return False
    del self._actions[key]
    if key in self._cache:
        del self._cache[key]
    return True