def readString(self, bytes=False):
    l = self.stream.read_ushort()
    b = self.stream.read(l)
    if bytes:
        return b
    return self.context.getStringForBytes(b)