def find_in_cache(cacheKey):
    if cacheKey:
        data = cache.get('plugit-cache-' + cacheKey, None)
        if data:
            return data['result'], data['menu'], data['context']
    return None, None, None