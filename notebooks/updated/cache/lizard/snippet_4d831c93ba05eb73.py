def values(self):
    if self._values is None:
        self._values = self.calculateValues()
    return self._values