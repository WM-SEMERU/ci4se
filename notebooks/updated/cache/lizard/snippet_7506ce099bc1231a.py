def native(self):
    if self.contents is None:
        return None
    if self._native is None:
        self._native = self.__int__()
        if self._map is not None and self._native in self._map:
            self._native = self._map[self._native]
    return self._native