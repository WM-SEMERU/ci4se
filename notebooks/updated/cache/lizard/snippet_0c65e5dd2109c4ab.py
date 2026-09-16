def read(self, n):
    if len(self.buf) == 0:
        self._recv()
    if len(self.buf) > 0:
        if n > len(self.buf):
            n = len(self.buf)
        ret = self.buf[:n]
        self.buf = self.buf[n:]
        if self._debug >= 2:
            for b in ret:
                self.debug('read 0x%x' % ord(b), 2)
        return ret
    return ''