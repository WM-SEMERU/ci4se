def expect(self, *args):
    t = self.accept(*args)
    if t is not None:
        return t
    self.error('expected: %r' % (args,))