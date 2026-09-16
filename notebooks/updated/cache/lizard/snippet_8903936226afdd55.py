def pairs(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)