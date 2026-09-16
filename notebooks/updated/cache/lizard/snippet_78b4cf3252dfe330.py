def next(self, skip=None):
    buffer = self._buffer
    popleft = buffer.popleft
    if skip is not None:
        while True:
            try:
                if not skip(buffer[0]):
                    break
                popleft()
            except IndexError:
                self._buffer_fill()
    try:
        datum = popleft()
    except IndexError:
        self._buffer_fill()
        datum = popleft()
    return datum