def copy(self, **kwargs):
    for k in kwargs:
        assert k in self._keys, 'Invalid key: %s' % k
    d = self.values()
    d.update(kwargs)
    return self.__class__(**d)