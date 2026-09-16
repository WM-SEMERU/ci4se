def _insert_row(self, i, index):
    if i == len(self._index):
        self._add_row(index)
    else:
        self._index.insert(i, index)
        self._data.insert(i, None)