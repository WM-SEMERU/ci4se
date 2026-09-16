def exact(self, *args, **kwargs):
    compare = Exact(*args, **kwargs)
    self.add(compare)
    return self