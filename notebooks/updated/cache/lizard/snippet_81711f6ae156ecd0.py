def unpack(self, fmt):
    sfmt = compile_struct(fmt)
    size = sfmt.size
    if not self.data:
        raise UnpackException(fmt, size, 0)
    buff = self.data.read(size)
    if len(buff) < size:
        raise UnpackException(fmt, size, len(buff))
    return sfmt.unpack(buff)