def _array_convert(a):
    from numpy import ndarray
    if isinstance(a, ndarray):
        larr = a.tolist()
        if len(larr) == 1:
            return larr[0]
        else:
            return larr
    else:
        return a