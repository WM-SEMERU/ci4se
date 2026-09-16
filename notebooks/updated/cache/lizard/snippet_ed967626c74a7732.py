def add_table(table_name, table, cache=False, cache_scope=_CS_FOREVER,
    copy_col=True):
    if isinstance(table, Callable):
        table = TableFuncWrapper(table_name, table, cache=cache,
            cache_scope=cache_scope, copy_col=copy_col)
    else:
        table = DataFrameWrapper(table_name, table, copy_col=copy_col)
    table.clear_cached()
    logger.debug('registering table {!r}'.format(table_name))
    _TABLES[table_name] = table
    return table