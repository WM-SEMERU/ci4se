def read(self, size=None):
    r = self._buffer
    self._buffer = bytes()
    if size is not None:
        size -= len(r)
    r = r + self._response.read(size)
    return r