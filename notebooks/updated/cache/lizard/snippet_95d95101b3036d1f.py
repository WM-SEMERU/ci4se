def size(self, size=None):
    if size is None:
        return self._size
    else:
        if not is_numeric(size):
            raise TypeError("size must be number, not '%s'" % str(size))
        self._size = size