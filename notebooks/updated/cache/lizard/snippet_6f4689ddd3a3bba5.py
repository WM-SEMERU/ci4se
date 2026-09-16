def put(self, lo, hi):
    self.buf.append(lo)
    self.buf.append(hi)
    self.pos += 1