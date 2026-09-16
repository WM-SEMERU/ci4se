def full_groupby(iterable, key=None):
    return groupby(sorted(iterable, key=key), key=key)