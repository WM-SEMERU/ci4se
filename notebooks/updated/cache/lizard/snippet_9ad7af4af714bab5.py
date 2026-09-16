def table_as_df(self, table_name):
    self.table_must_exist(table_name)
    query = 'SELECT * FROM `%s`' % table_name.lower()
    return pandas.read_sql(query, self.own_conn)