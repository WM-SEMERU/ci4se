def top(self):
    if self.vMerge is None or self.vMerge == ST_Merge.RESTART:
        return self._tr_idx
    return self._tc_above.top