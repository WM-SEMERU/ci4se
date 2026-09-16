def find_newline(self, size=-1):
    if size < 0:
        return self._buffer.find('\n', self._offset)
    return self._buffer.find('\n', self._offset, self._offset + size)