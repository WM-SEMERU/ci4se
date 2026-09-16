def first(self, skipna=None, keep_attrs=None):
    return self._first_or_last(duck_array_ops.first, skipna, keep_attrs)