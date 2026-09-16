def set_cache_expiry(response):
    if (response.cache_control.max_age is None and 'CACHE_DEFAULT_TIMEOUT' in
        config.cache):
        response.cache_control.max_age = config.cache['CACHE_DEFAULT_TIMEOUT']
    return response