def equal_args(*args, **kwargs):
    key = args
    if kwargs:
        key += _kwargs_separator + tuple(sorted(kwargs.items()))
    return key