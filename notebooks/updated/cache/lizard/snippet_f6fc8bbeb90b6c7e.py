def get_sampling_strategy(self, sensor_name):
    cache_key = self._get_strategy_cache_key(sensor_name)
    cached = self._strategy_cache.get(cache_key)
    if not cached:
        return resource.normalize_strategy_parameters('none')
    else:
        return cached