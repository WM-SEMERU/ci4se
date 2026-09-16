def to_numpy(self, dtype=None, copy=False):
    if is_datetime64tz_dtype(self.dtype) and dtype is None:
        dtype = 'object'
    result = np.asarray(self._values, dtype=dtype)
    if copy:
        result = result.copy()
    return result