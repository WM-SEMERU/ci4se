def write_uint16(self, value, little_endian=True):
    if little_endian:
        endian = '<'
    else:
        endian = '>'
    return self.pack('%sH' % endian, value)