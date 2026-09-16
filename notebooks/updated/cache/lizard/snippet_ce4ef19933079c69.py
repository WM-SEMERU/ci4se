def turn(self):
    first = self._data.pop(0)
    self._data.append(first)