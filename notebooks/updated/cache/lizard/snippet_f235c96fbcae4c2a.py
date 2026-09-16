def limit_x(self, limit_lower=None, limit_upper=None):
    if limit_lower is None and limit_upper is None:
        return self._limit_x
    elif hasattr(limit_lower, '__iter__'):
        self._limit_x = limit_lower[:2]
    else:
        self._limit_x = [limit_lower, limit_upper]
    if self._limit_x[0] == self._limit_x[1]:
        self._limit_x[1] += 1
    self._limit_x[0] -= self.mod_x
    self._limit_x[1] += self.mod_x