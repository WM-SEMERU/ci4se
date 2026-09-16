def write_bytes(self, data, n):
    for pos in xrange(0, n):
        self.payload[self.pos + pos] = data[pos]
    self.pos += n