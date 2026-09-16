def read_chunk(self, t):
    size = self.data[self.pos:self.pos + 4].cast('i')[0]
    d = self.data[self.pos + 4:self.pos + 4 + size]
    assert self.data[self.pos + 4 + size:self.pos + 4 + size + 4].cast('i')[0
        ] == size
    self.pos = self.pos + 4 + size + 4
    res = np.array(d.cast(t))
    if res.size == 1:
        return res[0]
    return res