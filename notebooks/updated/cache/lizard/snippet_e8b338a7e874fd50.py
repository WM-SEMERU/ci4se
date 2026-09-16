def encode(self):
    byte = self.default
    for bit, name, value0, value1, default in SeqCmdAttrs.Table:
        if name in self.attrs:
            value = self.attrs[name]
            byte = setBit(byte, bit, value == value1)
    return struct.pack('B', byte)