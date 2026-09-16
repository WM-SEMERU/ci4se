def set(self, val, lifetime=None):
    cache.set(self.key, json.dumps(val) if self.serialize else val, 
        lifetime or settings.DEFAULT_CACHE_EXPIRE_TIME)
    return val