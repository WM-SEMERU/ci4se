def _hash(expr, func=None):
    if func is None:
        func = lambda x: hash(x)
    return _map(expr, func=func, rtype=types.int64)