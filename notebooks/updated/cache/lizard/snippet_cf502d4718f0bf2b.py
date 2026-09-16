def _wrap(cls, func):
    if isinstance(func, cls):
        return func
    return functools.update_wrapper(cls(func), func)