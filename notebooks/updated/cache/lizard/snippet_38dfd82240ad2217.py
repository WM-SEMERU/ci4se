def _select_limit_statement(table, cols='*', offset=0, limit=MAX_ROWS_PER_QUERY
    ):
    return 'SELECT {0} FROM {1} LIMIT {2}, {3}'.format(join_cols(cols),
        wrap(table), offset, limit)