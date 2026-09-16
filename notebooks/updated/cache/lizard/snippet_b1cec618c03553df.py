def insert(self, index, filename):
    base = self._base
    dct = {'__module__': base.__module__, 'filename': filename, '_stack': self}
    cls = type(base.__name__, (base,), dct)
    self._map[cls.filename] = cls
    self._classes.insert(index, cls)