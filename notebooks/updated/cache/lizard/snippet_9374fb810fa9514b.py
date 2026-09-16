def rotate(self):
    self._index -= 1
    if self._index >= 0:
        return self._ring[self._index]
    return None