def fill_rawq(self):
    if self.irawq >= len(self.rawq):
        self.rawq = b''
        self.irawq = 0
    buf = yield from self._reader.read(50)
    self.eof = not buf
    self.rawq = self.rawq + buf