def column_exists(cr, table, column):
    cr.execute(
        'SELECT count(attname) FROM pg_attribute WHERE attrelid = ( SELECT oid FROM pg_class WHERE relname = %s ) AND attname = %s'
        , (table, column))
    return cr.fetchone()[0] == 1