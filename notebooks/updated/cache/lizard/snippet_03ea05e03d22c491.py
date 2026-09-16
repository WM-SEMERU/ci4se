def set_index(self, index):
    if index is None:
        pass
    elif isinstance(index, str):
        index = SortedIndex(self[index], copy=False)
    elif isinstance(index, (tuple, list)) and len(index) == 2:
        index = SortedMultiIndex(self[index[0]], self[index[1]], copy=False)
    else:
        raise ValueError(
            'invalid index argument, expected string or pair of strings, found %s'
             % repr(index))
    self.index = index