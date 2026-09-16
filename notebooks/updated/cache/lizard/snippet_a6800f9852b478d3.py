def filter(self, func):
    self._data = xfilter(func, self._data)
    return self