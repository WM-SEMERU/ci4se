def query(self, query, stacked=False):
    from jx_base.query import QueryOp
    query = QueryOp.wrap(query)
    sql, post = self._subquery(query, isolate=False, stacked=stacked)
    query.data = post(sql)
    return query.data