def main(self, din, reload):
    if reload:
        lfsr = self.INIT_GALOIS
    else:
        lfsr = self.lfsr
    out = lfsr & 32768
    next = (lfsr << 1 | din) & 65535
    if out != 0:
        next = next ^ self.XOR
    self.lfsr = next
    return self.lfsr