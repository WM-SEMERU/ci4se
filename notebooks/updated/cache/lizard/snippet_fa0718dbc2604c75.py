def read_byte(self):
    buf = b''
    if len(self.cookedq) > 0:
        buf = bytes([self.cookedq[0]])
        self.cookedq = self.cookedq[1:]
    else:
        yield from self.process_rawq()
        if not self.eof:
            yield from self.fill_rawq()
            yield from self.process_rawq()
            buf = yield from self.read_byte()
    return buf