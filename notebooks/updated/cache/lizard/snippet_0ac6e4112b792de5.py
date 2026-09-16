def _expand(self, pos):
    _lists = self._lists
    _index = self._index
    if len(_lists[pos]) > self._dual:
        _maxes = self._maxes
        _load = self._load
        _lists_pos = _lists[pos]
        half = _lists_pos[_load:]
        del _lists_pos[_load:]
        _maxes[pos] = _lists_pos[-1]
        _lists.insert(pos + 1, half)
        _maxes.insert(pos + 1, half[-1])
        del _index[:]
    elif _index:
        child = self._offset + pos
        while child:
            _index[child] += 1
            child = child - 1 >> 1
        _index[0] += 1