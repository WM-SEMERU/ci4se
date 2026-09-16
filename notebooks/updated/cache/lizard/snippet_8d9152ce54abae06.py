def memoize(f):

    def _c(*args, **kwargs):
        if not hasattr(f, 'cache'):
            f.cache = dict()
        key = args, tuple(kwargs)
        if key not in f.cache:
            f.cache[key] = f(*args, **kwargs)
        return f.cache[key]
    return wraps(f)(_c)