def merge(self, other_cell):
    tc, tc_2 = self._tc, other_cell._tc
    merged_tc = tc.merge(tc_2)
    return _Cell(merged_tc, self._parent)