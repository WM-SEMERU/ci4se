def process_response(self, request, response):
    if self._is_enabled():
        log_prefix = self._log_prefix('After', request)
        new_memory_data = self._memory_data(log_prefix)
        log_prefix = self._log_prefix('Diff', request)
        cached_memory_data_response = self._cache.get_cached_response(self.
            memory_data_key)
        old_memory_data = cached_memory_data_response.get_value_or_default(None
            )
        self._log_diff_memory_data(log_prefix, new_memory_data, old_memory_data
            )
    return response