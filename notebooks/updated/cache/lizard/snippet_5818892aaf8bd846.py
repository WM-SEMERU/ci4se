def groupby(iterable, key=None):
    groups = {}
    for item in iterable:
        if key is None:
            key_value = item
        else:
            key_value = key(item)
        groups.setdefault(key_value, []).append(item)
    return groups