def parse_bytes(self, bytestr, isfinal=True):
    with self._context():
        self.filename = None
        self.p.Parse(bytestr, isfinal)
    return self._root