def nunique(self, axis=0, dropna=True):
    axis = self._get_axis_number(axis) if axis is not None else 0
    return self._reduce_dimension(self._query_compiler.nunique(axis=axis,
        dropna=dropna))