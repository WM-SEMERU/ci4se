def pop_range(self, start, stop, callback=None, withscores=True):
    s1 = self.pickler.dumps(start)
    s2 = self.pickler.dumps(stop)
    backend = self.backend
    res = backend.structure(self).pop_range(s1, s2, withscores=withscores)
    if not callback:
        callback = self.load_data if withscores else self.load_values
    return backend.execute(res, callback)