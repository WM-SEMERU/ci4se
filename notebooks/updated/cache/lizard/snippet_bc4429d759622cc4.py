def restrict(self, point):
    items = [f.restrict(point) for f in self._items]
    return self.__class__(items, self.shape, self.ftype)