def index(self, value, start=0, end=None):
    try:
        index = self._dict[value]
    except KeyError:
        raise ValueError
    else:
        start = self._fix_neg_index(start)
        end = self._fix_end_index(end)
        if start <= index and index < end:
            return index
        else:
            raise ValueError