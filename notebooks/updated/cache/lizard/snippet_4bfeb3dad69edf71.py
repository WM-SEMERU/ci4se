def find_all(self, table_name, constraints=None, *, columns=None, order_by=
    None, limiting=None):
    query_string, params = self.sql_writer.get_find_all_query(table_name,
        constraints, columns=columns, order_by=order_by, limiting=limiting)
    query_string += ';'
    return self.execute(query_string, params)