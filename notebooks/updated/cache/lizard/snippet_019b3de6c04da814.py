def filter(objects, Type=None, min=-1, max=-1):
    res = []
    if min > max:
        raise ValueError('minimum must be smaller than maximum')
    if Type is not None:
        res = [o for o in objects if isinstance(o, Type)]
    if min > -1:
        res = [o for o in res if _getsizeof(o) < min]
    if max > -1:
        res = [o for o in res if _getsizeof(o) > max]
    return res