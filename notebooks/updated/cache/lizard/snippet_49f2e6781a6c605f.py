def cvt_iter(a):
    if a is None:
        return a
    if not isinstance(a, (tuple, list)):
        a = tuple(a)
    return a