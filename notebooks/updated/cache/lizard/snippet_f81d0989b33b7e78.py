def _unpickle_sparse_frame_compat(self, state):
    series, cols, idx, fv, kind = state
    if not isinstance(cols, Index):
        from pandas.io.pickle import _unpickle_array
        columns = _unpickle_array(cols)
    else:
        columns = cols
    if not isinstance(idx, Index):
        from pandas.io.pickle import _unpickle_array
        index = _unpickle_array(idx)
    else:
        index = idx
    series_dict = DataFrame()
    for col, (sp_index, sp_values) in series.items():
        series_dict[col] = SparseSeries(sp_values, sparse_index=sp_index,
            fill_value=fv)
    self._data = to_manager(series_dict, columns, index)
    self._default_fill_value = fv
    self._default_kind = kind