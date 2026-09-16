def _make_cache_key(key_prefix):
    if callable(key_prefix):
        cache_key = key_prefix()
    elif '%s' in key_prefix:
        cache_key = key_prefix % request.path
    else:
        cache_key = key_prefix
    cache_key = cache_key.encode('utf-8')
    return cache_key