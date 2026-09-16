def fetch_size(self, v):
    if not isinstance(v, six.integer_types):
        raise TypeError
    if v == self._fetch_size:
        return self
    if v < 1:
        raise QueryException('fetch size less than 1 is not allowed')
    clone = copy.deepcopy(self)
    clone._fetch_size = v
    return clone