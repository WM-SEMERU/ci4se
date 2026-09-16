def list_get(l, idx, default=None):
    try:
        if l[idx]:
            return l[idx]
        else:
            return default
    except IndexError:
        return default