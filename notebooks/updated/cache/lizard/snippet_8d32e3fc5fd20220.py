def _grow_to(self, width, height, top_tc=None):

    def vMerge_val(top_tc):
        if top_tc is not self:
            return ST_Merge.CONTINUE
        if height == 1:
            return None
        return ST_Merge.RESTART
    top_tc = self if top_tc is None else top_tc
    self._span_to_width(width, top_tc, vMerge_val(top_tc))
    if height > 1:
        self._tc_below._grow_to(width, height - 1, top_tc)