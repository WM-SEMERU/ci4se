def _read_sql_with_limit_offset(num_splits, sql, con, index_col, kwargs):
    pandas_df = pandas.read_sql(sql, con, index_col=index_col, **kwargs)
    if index_col is None:
        index = len(pandas_df)
    else:
        index = pandas_df.index
    return _split_result_for_readers(1, num_splits, pandas_df) + [index]