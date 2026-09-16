def read_sql(sql, con, index_col=None, coerce_float=True, params=None,
    parse_dates=None, columns=None, chunksize=None):
    pandas_sql = pandasSQL_builder(con)
    if isinstance(pandas_sql, SQLiteDatabase):
        return pandas_sql.read_query(sql, index_col=index_col, params=
            params, coerce_float=coerce_float, parse_dates=parse_dates,
            chunksize=chunksize)
    try:
        _is_table_name = pandas_sql.has_table(sql)
    except Exception:
        _is_table_name = False
    if _is_table_name:
        pandas_sql.meta.reflect(only=[sql])
        return pandas_sql.read_table(sql, index_col=index_col, coerce_float
            =coerce_float, parse_dates=parse_dates, columns=columns,
            chunksize=chunksize)
    else:
        return pandas_sql.read_query(sql, index_col=index_col, params=
            params, coerce_float=coerce_float, parse_dates=parse_dates,
            chunksize=chunksize)