def to_dict(self, index=True, ordered=False):
    result = OrderedDict() if ordered else dict()
    if index:
        result.update({self._index_name: self._index})
    if ordered:
        data_dict = [(self._data_name, self._data)]
    else:
        data_dict = {self._data_name: self._data}
    result.update(data_dict)
    return result