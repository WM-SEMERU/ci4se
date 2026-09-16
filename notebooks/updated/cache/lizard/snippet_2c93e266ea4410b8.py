def memoized_ignoreargs(func):

    def wrapper(*args, **kwargs):
        if func not in _MEMOIZED_NOARGS:
            res = func(*args, **kwargs)
            _MEMOIZED_NOARGS[func] = res
            return res
        return _MEMOIZED_NOARGS[func]
    return wrapper