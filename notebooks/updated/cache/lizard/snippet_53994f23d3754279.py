def count(self, val):
    _maxes = self._maxes
    if not _maxes:
        return 0
    key = self._key(val)
    pos = bisect_left(_maxes, key)
    if pos == len(_maxes):
        return 0
    _lists = self._lists
    _keys = self._keys
    idx = bisect_left(_keys[pos], key)
    total = 0
    len_keys = len(_keys)
    len_sublist = len(_keys[pos])
    while True:
        if _keys[pos][idx] != key:
            return total
        if _lists[pos][idx] == val:
            total += 1
        idx += 1
        if idx == len_sublist:
            pos += 1
            if pos == len_keys:
                return total
            len_sublist = len(_keys[pos])
            idx = 0