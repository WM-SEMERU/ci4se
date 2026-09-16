def lfu_cache(max_size=128):

    def actual_decorator(func):
        return _cached_func(func, caches.LFUCache, max_size)
    return actual_decorator