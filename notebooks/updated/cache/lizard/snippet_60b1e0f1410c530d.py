def invert(self):
    keys = self._clean.keys()
    inverted = {}
    for key in keys:
        inverted[self.obj[key]] = key
    return self._wrap(inverted)