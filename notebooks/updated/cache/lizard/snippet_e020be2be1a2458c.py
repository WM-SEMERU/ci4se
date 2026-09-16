def get_distributions(self):
    if not self._cache_enabled:
        for dist in self._yield_distributions():
            yield dist
    else:
        self._generate_cache()
        for dist in self._cache.path.values():
            yield dist
        if self._include_egg:
            for dist in self._cache_egg.path.values():
                yield dist