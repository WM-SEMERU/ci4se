def root(self, set=None):
    assert isinstance(set, (int, bool, type(None)))
    if set:
        self.root_ = True
    return self.root_