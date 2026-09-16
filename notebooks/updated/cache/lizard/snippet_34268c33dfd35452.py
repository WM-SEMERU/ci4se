def add(self, data, name=None):
    if name is None:
        n = len(self.data)
        while 'Series %d' % n in self.data:
            n += 1
        name = 'Series %d' % n
    self.data[name] = data
    return name