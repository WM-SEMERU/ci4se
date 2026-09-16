def all(self, axis=0, bool_only=None, skipna=True, level=None, **kwargs):
    if axis is not None:
        axis = self._get_axis_number(axis)
        if bool_only and axis == 0:
            if hasattr(self, 'dtype'):
                raise NotImplementedError(
                    '{}.{} does not implement numeric_only.'.format(self.
                    __name__, 'all'))
            data_for_compute = self[self.columns[self.dtypes == np.bool]]
            return data_for_compute.all(axis=axis, bool_only=False, skipna=
                skipna, level=level, **kwargs)
        return self._reduce_dimension(self._query_compiler.all(axis=axis,
            bool_only=bool_only, skipna=skipna, level=level, **kwargs))
    else:
        if bool_only:
            raise ValueError('Axis must be 0 or 1 (got {})'.format(axis))
        result = self._reduce_dimension(self._query_compiler.all(axis=0,
            bool_only=bool_only, skipna=skipna, level=level, **kwargs))
        if isinstance(result, BasePandasDataset):
            return result.all(axis=axis, bool_only=bool_only, skipna=skipna,
                level=level, **kwargs)
        return result