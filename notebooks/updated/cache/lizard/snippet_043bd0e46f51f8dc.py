def to_numpy(self, dtype=None, copy=False):
    return self._default_to_pandas('to_numpy', dtype=dtype, copy=copy)