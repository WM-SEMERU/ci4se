def get_foreign_key_base_declaration_sql(self, foreign_key):
    sql = ''
    if foreign_key.get_name():
        sql += 'CONSTRAINT %s ' % foreign_key.get_quoted_name(self)
    sql += 'FOREIGN KEY ('
    if not foreign_key.get_local_columns():
        raise DBALException('Incomplete definition. "local" required.')
    if not foreign_key.get_foreign_columns():
        raise DBALException('Incomplete definition. "foreign" required.')
    if not foreign_key.get_foreign_table_name():
        raise DBALException('Incomplete definition. "foreign_table" required.')
    sql += '%s) REFERENCES %s (%s)' % (', '.join(foreign_key.
        get_quoted_local_columns(self)), foreign_key.
        get_quoted_foreign_table_name(self), ', '.join(foreign_key.
        get_quoted_foreign_columns(self)))
    return sql