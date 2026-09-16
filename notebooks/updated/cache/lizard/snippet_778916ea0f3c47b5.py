def iter_points(x):
    if isinstance(x, (list, tuple)):
        if len(x):
            if isinstance(x[0], (list, tuple)):
                out = []
                for y in x:
                    out += iter_points(y)
                return out
            else:
                return [x]
        else:
            return []
    else:
        raise ValueError('List/tuple type expected. Got {!r}.'.format(x))