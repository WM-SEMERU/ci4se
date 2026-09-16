def _create_table(self, table_name, column_types, primary=None, nullable=()):
    require_string(table_name, 'table name')
    require_iterable_of(column_types, tuple, name='rows')
    if primary is not None:
        require_string(primary, 'primary')
    require_iterable_of(nullable, str, name='nullable')
    column_decls = []
    for column_name, column_type in column_types:
        decl = '%s %s' % (column_name, column_type)
        if column_name == primary:
            decl += ' UNIQUE PRIMARY KEY'
        if column_name not in nullable:
            decl += ' NOT NULL'
        column_decls.append(decl)
    column_decl_str = ', '.join(column_decls)
    create_table_sql = 'CREATE TABLE %s (%s)' % (table_name, column_decl_str)
    self.execute_sql(create_table_sql)