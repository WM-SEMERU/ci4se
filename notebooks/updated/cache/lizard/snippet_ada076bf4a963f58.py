def recover(self, key, value):
    if key not in self._dtypes:
        self.read_types()
    if key not in self._dtypes:
        raise ValueError('Unknown datatype for {} and {}'.format(key, value))
    return self._dtypes[key][2](value)