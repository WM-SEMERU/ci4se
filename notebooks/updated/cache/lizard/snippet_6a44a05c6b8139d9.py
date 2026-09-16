def table(name=None, mode='create', use_cache=True, priority='interactive',
    allow_large_results=False):
    output = QueryOutput()
    output._output_type = 'table'
    output._table_name = name
    output._table_mode = mode
    output._use_cache = use_cache
    output._priority = priority
    output._allow_large_results = allow_large_results
    return output