def _cache_init(self):
    cache_ = cache.get(self.CACHE_KEY)
    if cache_ is None:
        cache_ = defaultdict(dict)
    self._cache = cache_