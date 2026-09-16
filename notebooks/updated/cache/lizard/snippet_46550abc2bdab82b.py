def clear_caches(self):
    self.get_repository.cache_clear()
    self._get_repository.cache_clear()
    self.pool.clear_caches()