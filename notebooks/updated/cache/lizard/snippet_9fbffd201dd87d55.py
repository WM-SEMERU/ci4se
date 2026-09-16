def execute_sql(self, result_type=constants.MULTI, chunked_fetch=False,
    chunk_size=constants.GET_ITERATOR_CHUNK_SIZE):
    try:
        sql, params = self.as_sql()
        if not sql:
            raise EmptyResultSet
    except EmptyResultSet:
        if result_type == constants.MULTI:
            return iter([])
        else:
            return
    cursor = self.connection.cursor()
    cursor.prepare_query(self.query)
    cursor.execute(sql, params)
    if not result_type or result_type == 'cursor':
        return cursor
    if result_type == constants.SINGLE:
        return cursor.fetchone()
    result = iter(lambda : cursor.fetchmany(chunk_size), self.connection.
        features.empty_fetchmany_value)
    if (not chunked_fetch and not self.connection.features.
        can_use_chunked_reads):
        return list(result)
    return result