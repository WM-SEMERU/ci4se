def uniform(low=0, high=1, shape=_Null, dtype=_Null, ctx=None, out=None, **
    kwargs):
    return _random_helper(_internal._random_uniform, _internal.
        _sample_uniform, [low, high], shape, dtype, ctx, out, kwargs)