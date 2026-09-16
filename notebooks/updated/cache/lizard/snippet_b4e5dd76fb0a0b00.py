def get_cached_source_variable(self, source_id, variable, default=None):
    source_id = int(source_id)
    try:
        return self._retrieve_cached_source_variable(source_id, variable)
    except UncachedVariable:
        return default