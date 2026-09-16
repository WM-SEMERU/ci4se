def cacheOnSameArgs(timeout=None):
    if isinstance(timeout, int):
        timeout = datetime.timedelta(0, timeout)

    def decorator(f):
        _cache = [None]

        def wrapper(*args, **kwargs):
            if _cache[0] is not None:
                cached_ret, dt, cached_args, cached_kwargs = _cache[0]
                if (timeout is not None and dt + timeout <= datetime.
                    datetime.now()):
                    _cache[0] = None
                if (cached_args, cached_kwargs) != (args, kwargs):
                    _cache[0] = None
            if _cache[0] is None:
                ret = f(*args, **kwargs)
                _cache[0] = ret, datetime.datetime.now(), args, kwargs
            return _cache[0][0]
        return wrapper
    return decorator