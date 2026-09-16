def keys_in(items, *args):
    found = dict((key, False) for key in items)
    for d in args:
        for item in items:
            if not found[item] and item in d:
                found[item] = True
    return all(found.values())