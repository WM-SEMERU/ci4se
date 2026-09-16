def ones(shape, dtype=None, **kwargs):
    if dtype is None:
        dtype = _numpy.float32
    return _internal._ones(shape=shape, dtype=dtype, **kwargs)