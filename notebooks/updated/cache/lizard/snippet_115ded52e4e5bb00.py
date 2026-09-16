def drop_table(dbo, tablename, schema=None, commit=True):
    tablename = _quote(tablename)
    if schema is not None:
        tablename = _quote(schema) + '.' + tablename
    sql = 'DROP TABLE %s' % tablename
    _execute(sql, dbo, commit)