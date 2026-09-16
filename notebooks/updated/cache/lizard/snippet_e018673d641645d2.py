def search_command_record(self, after_context, before_context, context,
    context_type, **kwds):
    if after_context or before_context or context:
        kwds['condition_as_column'] = True
        limit = kwds['limit']
        kwds['limit'] = -1
        kwds['unique'] = False
        kwds['sort_by'] = {'session': ['session_start_time', 'start_time'],
            'time': ['start_time']}[context_type]
        if not kwds['reverse']:
            after_context, before_context = before_context, after_context
    sql, params, keys = self._compile_sql_search_command_record(**kwds)
    records = self._select_rows(CommandRecord, keys, sql, params)
    predicate = lambda r: r.condition
    if context:
        records = include_context(predicate, context, records)
    elif before_context:
        records = include_before(predicate, before_context, records)
    elif after_context:
        records = include_after(predicate, after_context, records)
    if after_context or before_context or context and limit >= 0:
        records = itertools.islice(records, limit)
    return records