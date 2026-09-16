def count(self, table_name, constraints=None, *, extract='index'):
    where, params = self.sql_writer.parse_constraints(constraints)
    sql = 'select count(*) as count from {0} where {1};'.format(table_name,
        where or '1 = 1')
    return self.get_scalar(self.execute(sql, params), 0 if extract ==
        'index' else 'count')