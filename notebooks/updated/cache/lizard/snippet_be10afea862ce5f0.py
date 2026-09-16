def limit(self, n):
    data = self._data
    self._data = (next(data) for _ in xrange(int(round(n))))
    return self