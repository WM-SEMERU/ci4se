def read_long(self):
    self.bitcount = self.bits = 0
    return unpack('>I', self.input.read(4))[0]