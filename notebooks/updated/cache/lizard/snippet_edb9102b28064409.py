def read_line(self, sep=six.b('\n')):
    start = 0
    while not self._stream.closed:
        loc = self._buffer.find(sep, start)
        if loc >= 0:
            return self._pop(loc + len(sep))
        else:
            start = len(self._buffer)
        self._buffer += self._stream.read(self._chunk_size)
    return six.b('')