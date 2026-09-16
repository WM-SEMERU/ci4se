def collect_by_type(obj_sequence, cache=None):
    if cache is None:
        cache = {}
    for val in obj_sequence:
        key = type(val)
        bucket = cache.get(key, None)
        if bucket is not None:
            bucket.append(val)
        else:
            cache[key] = [val]
    return cache