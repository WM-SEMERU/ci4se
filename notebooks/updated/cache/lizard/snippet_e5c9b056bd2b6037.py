def _show_tables(self, *args):
    v = self.connection.lowest_server_version
    schema_name = ('table_schema' if v >= TABLE_SCHEMA_MIN_VERSION else
        'schema_name')
    table_filter = (" AND table_type = 'BASE TABLE'" if v >=
        TABLE_TYPE_MIN_VERSION else '')
    self._exec(
        "SELECT format('%s.%s', {schema}, table_name) AS name FROM information_schema.tables WHERE {schema} NOT IN ('sys','information_schema', 'pg_catalog'){table_filter}"
        .format(schema=schema_name, table_filter=table_filter))