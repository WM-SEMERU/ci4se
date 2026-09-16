def accumulate(self, buf):
    accum = self.crc
    for b in buf:
        tmp = b ^ accum & 255
        tmp = (tmp ^ tmp << 4) & 255
        accum = accum >> 8 ^ tmp << 8 ^ tmp << 3 ^ tmp >> 4
    self.crc = accum