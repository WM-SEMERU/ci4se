def _read(self, length):
    bytes = self.read(length)
    if len(bytes) != length:
        self.seek(0 - len(bytes), 1)
        raise IOError('Tried to read %d byte(s) from the stream' % length)
    return bytes