def remove(self, key):
    self._vertices.remove(key)
    for f in self._forwards.pop(key):
        self._backwards[f].remove(key)
    for t in self._backwards.pop(key):
        self._forwards[t].remove(key)