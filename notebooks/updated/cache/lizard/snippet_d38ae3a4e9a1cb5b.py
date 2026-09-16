def previous_key(self, cache_key):
    if not self.cacheable(cache_key):
        return None
    previous_hash = self._read_sha(cache_key)
    if not previous_hash:
        return None
    return CacheKey(cache_key.id, previous_hash)