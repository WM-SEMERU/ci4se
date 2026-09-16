def pack(self):
    sn, sa = self.number, self.attribute
    return pack('<H', (sn & 1023) << 6 | sa & 63)