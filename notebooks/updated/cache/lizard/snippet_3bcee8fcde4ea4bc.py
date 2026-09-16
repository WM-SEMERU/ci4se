def enable_caching(self, file_path=None):
    if not file_path:
        file_path = tempfile.mktemp(prefix='pylast_tmp_')
    self.cache_backend = _ShelfCacheBackend(file_path)