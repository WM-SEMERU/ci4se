def bytes(self, count):
    if count < 0:
        raise ValueError
    if self._bits == 0:
        data = self._fileobj.read(count)
        if len(data) != count:
            raise BitReaderError('not enough data')
        return data
    return bytes(bytearray(self.bits(8) for _ in xrange(count)))