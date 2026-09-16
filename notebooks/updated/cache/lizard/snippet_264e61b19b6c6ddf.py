def multisorted(items, *keys):
    if len(keys) == 0:
        keys = [asc()]
    for key in reversed(keys):
        items = sorted(items, key=key.func, reverse=key.reverse)
    return items