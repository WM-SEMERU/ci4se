def process(self, c):
    if isinstance(c, bytes):
        c = self._decode(c)
    self.state.process(c)