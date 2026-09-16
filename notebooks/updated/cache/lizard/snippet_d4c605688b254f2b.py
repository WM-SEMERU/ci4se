def read_float(self):
    self.bitcount = self.bits = 0
    return unpack('>d', self.input.read(8))[0]