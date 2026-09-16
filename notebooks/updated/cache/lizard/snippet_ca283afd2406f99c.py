def insert(self, i, *nodes):
    r
    assert isinstance(i, int
        ), 'Provided index "{}" is not an integer! Did you switch your arguments? The first argument to `insert` is the index.'.format(
        i)
    self.expr.insert(i, *nodes)