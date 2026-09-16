def unload_key(self, key):
    key_hash = self._hash_for_key(key)
    if key in self:
        del self._cache[key_hash]