def cycle_app_reverse_cache(*args, **kwargs):
    value = '%07x' % SystemRandom().randint(0, 268435456)
    cache.set(APP_REVERSE_CACHE_GENERATION_KEY, value)
    return value