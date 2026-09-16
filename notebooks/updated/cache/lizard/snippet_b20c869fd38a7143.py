def get_entire_column(self, column, as_list=False):
    c = self._columns.index(column)
    data = self._data[c]
    return data if as_list else DataFrame(data={column: data}, index=self.
        _index, index_name=self._index_name, sort=self._sort)