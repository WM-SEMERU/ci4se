def mean(array, axis=None, skipna=None, **kwargs):
    from .common import _contains_cftime_datetimes
    array = asarray(array)
    if array.dtype.kind in 'Mm':
        offset = min(array)
        dtype = 'timedelta64[ns]'
        return _mean(datetime_to_numeric(array, offset), axis=axis, skipna=
            skipna, **kwargs).astype(dtype) + offset
    elif _contains_cftime_datetimes(array):
        if isinstance(array, dask_array_type):
            raise NotImplementedError(
                'Computing the mean of an array containing cftime.datetime objects is not yet implemented on dask arrays.'
                )
        offset = min(array)
        timedeltas = datetime_to_numeric(array, offset, datetime_unit='us')
        mean_timedeltas = _mean(timedeltas, axis=axis, skipna=skipna, **kwargs)
        return _to_pytimedelta(mean_timedeltas, unit='us') + offset
    else:
        return _mean(array, axis=axis, skipna=skipna, **kwargs)