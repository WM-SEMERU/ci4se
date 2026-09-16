def build_select_fields(self):
    field_sql = []
    for table in self.tables:
        field_sql += table.get_field_sql()
    for join_item in self.joins:
        field_sql += join_item.right_table.get_field_sql()
    sql = 'SELECT {0}{1} '.format(self.get_distinct_sql(), ', '.join(field_sql)
        )
    return sql