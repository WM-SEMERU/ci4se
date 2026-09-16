def string(self, *args, **kwargs):
    compare = String(*args, **kwargs)
    self.add(compare)
    return self