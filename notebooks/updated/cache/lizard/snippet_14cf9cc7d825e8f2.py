def size(self, value):
    if self._size != value and isinstance(value, (int, float, long)):
        self._size = value