def short_dask_repr(array, show_dtype=True):
    chunksize = tuple(c[0] for c in array.chunks)
    if show_dtype:
        return 'dask.array<shape={}, dtype={}, chunksize={}>'.format(array.
            shape, array.dtype, chunksize)
    else:
        return 'dask.array<shape={}, chunksize={}>'.format(array.shape,
            chunksize)