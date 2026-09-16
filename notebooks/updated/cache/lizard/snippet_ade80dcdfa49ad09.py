def objective_value(self):
    if self._f is None:
        raise RuntimeError('Problem has not been optimized yet')
    if self.direction == 'max':
        return -self._f + self.offset
    else:
        return self._f + self.offset