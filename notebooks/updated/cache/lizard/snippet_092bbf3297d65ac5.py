def all_table_names_in_schema(self, schema, cache=False, cache_timeout=None,
    force=False):
    tables = []
    try:
        tables = self.db_engine_spec.get_table_names(inspector=self.
            inspector, schema=schema)
    except Exception as e:
        logging.exception(e)
    return tables