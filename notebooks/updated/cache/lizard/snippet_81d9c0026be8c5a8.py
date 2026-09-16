def _upsample(self, method, limit=None, fill_value=None):
    self._set_binner()
    if self.axis:
        raise AssertionError('axis must be 0')
    if self._from_selection:
        raise ValueError(
            'Upsampling from level= or on= selection is not supported, use .set_index(...) to explicitly set index to datetime-like'
            )
    ax = self.ax
    obj = self._selected_obj
    binner = self.binner
    res_index = self._adjust_binner_for_upsample(binner)
    if limit is None and to_offset(ax.inferred_freq) == self.freq:
        result = obj.copy()
        result.index = res_index
    else:
        result = obj.reindex(res_index, method=method, limit=limit,
            fill_value=fill_value)
    result = self._apply_loffset(result)
    return self._wrap_result(result)