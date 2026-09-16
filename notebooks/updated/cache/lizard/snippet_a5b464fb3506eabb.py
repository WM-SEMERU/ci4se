def get_table_columns(self):
    query = 'SELECT * FROM "{schema}"."{table}" limit 0'.format(table=self.
        table_name, schema=self.schema)
    return get_columns(self.cc, query)