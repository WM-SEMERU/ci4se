def free_cache(ctx, *elts):
    for elt in elts:
        if isinstance(elt, Hashable):
            cache = __STATIC_ELEMENTS_CACHE__
        else:
            cache = __UNHASHABLE_ELTS_CACHE__
            elt = id(elt)
        if elt in cache:
            del cache[elt]
    if not elts:
        __STATIC_ELEMENTS_CACHE__.clear()
        __UNHASHABLE_ELTS_CACHE__.clear()