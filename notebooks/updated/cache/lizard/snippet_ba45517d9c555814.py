def cached_method(func):

    @functools.wraps(func)
    def wrapper(self, *args):
        if not hasattr(self, '_cache'):
            self._cache = {}
        key = _argstring((func.__name__,) + args)
        if key not in self._cache:
            self._cache[key] = func(self, *args)
        return self._cache[key]
    return wrapper