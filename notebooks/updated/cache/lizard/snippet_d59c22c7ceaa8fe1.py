def setdefault(self, key, default=None):
    self._wlock.acquire()
    try:
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default
    finally:
        self._wlock.release()