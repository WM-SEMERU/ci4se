def rawq_getchar(self):
    if not self.rawq:
        self.fill_rawq()
        if self.eof:
            raise EOFError
    c = self.rawq[self.irawq]
    if not py2:
        c = c.to_bytes((c.bit_length() + 7) // 8, 'big')
    self.irawq += 1
    if self.irawq >= len(self.rawq):
        self.rawq = b''
        self.irawq = 0
    return c