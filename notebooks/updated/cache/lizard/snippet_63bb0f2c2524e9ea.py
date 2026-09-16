def readline(self, fmt=None):
    prefix_size = self._fix()
    if fmt is None:
        content = self.read(prefix_size)
    else:
        fmt = self.endian + fmt
        fmt = _replace_star(fmt, prefix_size)
        content = struct.unpack(fmt, self.read(prefix_size))
    try:
        suffix_size = self._fix()
    except EOFError:
        suffix_size = -1
    if prefix_size != suffix_size:
        raise IOError(_FIX_ERROR)
    return content