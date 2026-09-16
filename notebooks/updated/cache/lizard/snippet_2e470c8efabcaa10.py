def rolling_window(array, length):
    orig_shape = array.shape
    if not orig_shape:
        raise IndexError("Can't restride a scalar.")
    elif orig_shape[0] <= length:
        raise IndexError(
            "Can't restride array of shape {shape} with a window length of {len}"
            .format(shape=orig_shape, len=length))
    num_windows = orig_shape[0] - length + 1
    new_shape = (num_windows, length) + orig_shape[1:]
    new_strides = (array.strides[0],) + array.strides
    return as_strided(array, new_shape, new_strides)