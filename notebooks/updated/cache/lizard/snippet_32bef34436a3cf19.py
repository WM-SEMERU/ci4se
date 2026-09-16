def n1ql_query(self, query, *args, **kwargs):
    if not isinstance(query, N1QLQuery):
        query = N1QLQuery(query)
    itercls = kwargs.pop('itercls', N1QLRequest)
    return itercls(query, self, *args, **kwargs)