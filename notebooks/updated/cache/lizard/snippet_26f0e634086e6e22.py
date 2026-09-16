def get_cell(self, index, column):
    i = sorted_index(self._index, index) if self._sort else self._index.index(
        index)
    c = self._columns.index(column)
    return self._data[c][i]