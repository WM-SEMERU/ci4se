def discard(self, val):
    _maxes = self._maxes
    if not _maxes:
        return
    pos = bisect_left(_maxes, val)
    if pos == len(_maxes):
        return
    _lists = self._lists
    idx = bisect_left(_lists[pos], val)
    if _lists[pos][idx] == val:
        self._delete(pos, idx)