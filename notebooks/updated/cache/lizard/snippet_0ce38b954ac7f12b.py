def _get_unique_index(self, dropna=False):
    if self.is_unique and not dropna:
        return self
    values = self.values
    if not self.is_unique:
        values = self.unique()
    if dropna:
        try:
            if self.hasnans:
                values = values[~isna(values)]
        except NotImplementedError:
            pass
    return self._shallow_copy(values)