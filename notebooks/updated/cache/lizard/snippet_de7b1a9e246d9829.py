def ReleaseFileSystem(self, file_system):
    identifier, cache_value = self._file_system_cache.GetCacheValueByObject(
        file_system)
    if not identifier:
        raise RuntimeError('Object not cached.')
    if not cache_value:
        raise RuntimeError('Invalid cache value.')
    self._file_system_cache.ReleaseObject(identifier)
    result = cache_value.IsDereferenced()
    if result:
        self._file_system_cache.RemoveObject(identifier)
    return result