def get_collation(self):
    buf = readall(self, Collation.wire_size)
    return Collation.unpack(buf)