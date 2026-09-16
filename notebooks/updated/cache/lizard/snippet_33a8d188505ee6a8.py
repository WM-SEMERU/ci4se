def contains(cat, key, container):
    hash(key)
    try:
        loc = cat.categories.get_loc(key)
    except KeyError:
        return False
    if is_scalar(loc):
        return loc in container
    else:
        return any(loc_ in container for loc_ in loc)