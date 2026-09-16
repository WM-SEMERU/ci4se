def read1(self, size=-1):
    self._check_can_read()
    if size is None:
        raise TypeError('Read size should be an integer, not None')
    if size == 0 or self._mode == _MODE_READ_EOF or not self._fill_buffer():
        return b''
    if 0 < size < len(self._buffer):
        data = self._buffer[:size]
        self._buffer = self._buffer[size:]
    else:
        data = self._buffer
        self._buffer = None
    self._pos += len(data)
    return data