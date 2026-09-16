def add(self, item):
    self._check_index()
    self._history = self._history[:self._index + 1]
    self._history.append(item)
    self._index += 1
    self._check_index()
    assert id(self.current_item) == id(item)