def load_iterable(self, iterable, session=None):
    data = []
    load = self.loads
    for v in iterable:
        data.append(load(v))
    return data