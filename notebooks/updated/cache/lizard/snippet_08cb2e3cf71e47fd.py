def asum(data, axis=None, mapper=None, blen=None, storage=None, create=
    'array', **kwargs):
    return reduce_axis(data, axis=axis, reducer=np.sum, block_reducer=np.
        add, mapper=mapper, blen=blen, storage=storage, create=create, **kwargs
        )