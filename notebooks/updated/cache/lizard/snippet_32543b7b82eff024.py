def set(self, ctype, key, data):
    with zvmutils.acquire_lock(self._lock):
        target_cache = self._get_ctype_cache(ctype)
        target_cache['data'][key] = data