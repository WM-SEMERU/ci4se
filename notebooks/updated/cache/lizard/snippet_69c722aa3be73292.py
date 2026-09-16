def all_schema_names(self, cache=False, cache_timeout=None, force=False):
    return self.db_engine_spec.get_schema_names(self.inspector)