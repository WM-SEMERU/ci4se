def _na_for_min_count(values, axis):
    if is_numeric_dtype(values):
        values = values.astype('float64')
    fill_value = na_value_for_dtype(values.dtype)
    if values.ndim == 1:
        return fill_value
    else:
        result_shape = values.shape[:axis] + values.shape[axis + 1:]
        result = np.empty(result_shape, dtype=values.dtype)
        result.fill(fill_value)
        return result