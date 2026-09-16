def drop_duplicates(self, subset=None, keep='first', inplace=False):
    if self.empty:
        return self.copy()
    inplace = validate_bool_kwarg(inplace, 'inplace')
    duplicated = self.duplicated(subset, keep=keep)
    if inplace:
        inds, = (-duplicated)._ndarray_values.nonzero()
        new_data = self._data.take(inds)
        self._update_inplace(new_data)
    else:
        return self[-duplicated]