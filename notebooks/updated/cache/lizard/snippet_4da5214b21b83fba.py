def map(self, func, value_shape=None, dtype=None):
    mapped = self.values.map(func, value_shape=value_shape, dtype=dtype)
    return self._constructor(mapped).__finalize__(self, noprop=('dtype',))