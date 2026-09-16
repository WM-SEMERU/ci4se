def set_to_cache(vk):
    v, k = vk
    try:
        cache.set(k, json.dumps(v), settings.CACHE_EXPIRE_DURATION)
    except Exception as e:
        pass
    return v, k