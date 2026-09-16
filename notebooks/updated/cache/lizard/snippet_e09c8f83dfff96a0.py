def hmset_dict(self, key, *args, **kwargs):
    if not args and not kwargs:
        raise TypeError('args or kwargs must be specified')
    pairs = ()
    if len(args) > 1:
        raise TypeError('single positional argument allowed')
    elif len(args) == 1:
        if not isinstance(args[0], dict):
            raise TypeError('args[0] must be dict')
        elif not args[0] and not kwargs:
            raise ValueError('args[0] is empty dict')
        pairs = chain.from_iterable(args[0].items())
    kwargs_pairs = chain.from_iterable(kwargs.items())
    return wait_ok(self.execute(b'HMSET', key, *chain(pairs, kwargs_pairs)))