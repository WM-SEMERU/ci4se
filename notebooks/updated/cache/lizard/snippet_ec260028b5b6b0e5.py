def get_query_kwargs(**kwargs):
    query_kwargs = {}
    query = kwargs.pop('query')
    if query:
        query_kwargs['query'] = query
    return query_kwargs