def ensure_ndarray(ndarray_or_adjusted_array):
    if isinstance(ndarray_or_adjusted_array, ndarray):
        return ndarray_or_adjusted_array
    elif isinstance(ndarray_or_adjusted_array, AdjustedArray):
        return ndarray_or_adjusted_array.data
    else:
        raise TypeError("Can't convert %s to ndarray" % type(
            ndarray_or_adjusted_array).__name__)