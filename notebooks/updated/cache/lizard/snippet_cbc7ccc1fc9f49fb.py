def triads(key):
    if _triads_cache.has_key(key):
        return _triads_cache[key]
    res = map(lambda x: triad(x, key), keys.get_notes(key))
    _triads_cache[key] = res
    return res