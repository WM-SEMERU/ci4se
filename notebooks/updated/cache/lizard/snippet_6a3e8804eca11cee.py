def cache(*depends_on):

    def cache_decorator(fn):

        @memoize
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if cache.disabled:
                return fn(*args, **kwargs)
            else:
                return _cache.get_value(fn, depends_on, args, kwargs)
        return wrapper
    return cache_decorator