def itermerged(self):
    for key in self:
        val = self._container[key.lower()]
        yield val[0], ', '.join(val[1:])