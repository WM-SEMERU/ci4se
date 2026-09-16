def _find_line_start_index(self, index):
    indexes = self._line_start_indexes
    pos = bisect.bisect_right(indexes, index) - 1
    return pos, indexes[pos]