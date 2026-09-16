def zeros(stype, shape, ctx=None, dtype=None, **kwargs):
    if stype == 'default':
        return _zeros_ndarray(shape, ctx=ctx, dtype=dtype, **kwargs)
    if ctx is None:
        ctx = current_context()
    dtype = mx_real_t if dtype is None else dtype
    if stype in ('row_sparse', 'csr'):
        aux_types = _STORAGE_AUX_TYPES[stype]
    else:
        raise ValueError('unknown storage type' + stype)
    out = _ndarray_cls(_new_alloc_handle(stype, shape, ctx, True, dtype,
        aux_types))
    return _internal._zeros(shape=shape, ctx=ctx, dtype=dtype, out=out, **
        kwargs)