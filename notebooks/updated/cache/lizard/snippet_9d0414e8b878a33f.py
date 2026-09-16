def append(self, *other):
    self._data = it.chain(self._data, Stream(*other)._data)
    return self