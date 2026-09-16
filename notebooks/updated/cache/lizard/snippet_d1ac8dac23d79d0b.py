def extend(self, items):
    items = np.array(items)
    pos = items.shape[0] + self.logical_size
    if pos > self.physical_size:
        amt = self._tmp_size()
        if self.physical_size + amt < pos:
            amt = pos - self.physical_size
        self._grow(amt=amt)
    stop = self._position + items.shape[0]
    self._data[self._position:stop] = items
    self._position += items.shape[0]
    return self