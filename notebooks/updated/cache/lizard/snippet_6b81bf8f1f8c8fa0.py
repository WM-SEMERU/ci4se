def is_cached(self, version=None):
    version = _process_version(self, version)
    if self.api.cache and self.api.cache.fs.isfile(self.get_version_path(
        version)):
        return True
    return False