def _maybe_coerce_values(self, values):
    if values.dtype != _NS_DTYPE:
        values = conversion.ensure_datetime64ns(values)
    if isinstance(values, DatetimeArray):
        values = values._data
    assert isinstance(values, np.ndarray), type(values)
    return values