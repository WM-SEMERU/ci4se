def _get_read_query(self, table_columns, limit=None):
    query_columns = [column.name for column in table_columns]
    query_columns.remove('the_geom_webmercator')
    query = 'SELECT {columns} FROM "{schema}"."{table_name}"'.format(table_name
        =self.table_name, schema=self.schema, columns=', '.join(query_columns))
    if limit is not None:
        if isinstance(limit, int) and limit >= 0:
            query += ' LIMIT {limit}'.format(limit=limit)
        else:
            raise ValueError('`limit` parameter must an integer >= 0')
    return query