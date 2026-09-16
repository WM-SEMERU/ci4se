def unpack(self, fmt):
    sfmt = compile_struct(fmt)
    size = sfmt.size
    offset = self.offset
    if self.data:
        avail = len(self.data) - offset
    else:
        avail = 0
    if avail < size:
        raise UnpackException(fmt, size, avail)
    self.offset = offset + size
    return sfmt.unpack_from(self.data, offset)