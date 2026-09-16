def _nanmean_ddof_object(ddof, value, axis=None, **kwargs):
    from .duck_array_ops import count, fillna, _dask_or_eager_func, where_method
    valid_count = count(value, axis=axis)
    value = fillna(value, 0)
    dtype = kwargs.pop('dtype', None)
    if dtype is None and value.dtype.kind == 'O':
        dtype = value.dtype if value.dtype.kind in ['cf'] else float
    data = _dask_or_eager_func('sum')(value, axis=axis, dtype=dtype, **kwargs)
    data = data / (valid_count - ddof)
    return where_method(data, valid_count != 0)