def s2n(self, offset, length, signed=0):
    self.file.seek(self.offset + offset)
    sliced = self.file.read(length)
    if self.endian == 'I':
        val = s2n_intel(sliced)
    else:
        val = s2n_motorola(sliced)
    if signed:
        msb = 1 << 8 * length - 1
        if val & msb:
            val -= msb << 1
    return val