def complex_dtype(dtype, default=None):
    dtype, dtype_in = np.dtype(dtype), dtype
    if is_complex_floating_dtype(dtype):
        return dtype
    try:
        complex_base_dtype = TYPE_MAP_R2C[dtype.base]
    except KeyError:
        if default is not None:
            return default
        else:
            raise ValueError('no complex counterpart exists for `dtype` {}'
                .format(dtype_repr(dtype_in)))
    else:
        return np.dtype((complex_base_dtype, dtype.shape))