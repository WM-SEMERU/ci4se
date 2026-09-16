def encode(self):
    ret = bytearray()
    for name, len, typecode in self.format:
        value = getattr(self, name)
        buf = struct.pack('<' + typecode, value)
        ret.extend(buf)
    return bytes(ret)