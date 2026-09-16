def _build_url(cls, request, path=None, **changes):
    changes = {k: v for k, v in changes.items() if v is not None}
    queries = {**request.url.query, **changes}
    queries = {k: v for k, v in queries.items() if v is not False}
    query_strings = []

    def add_query(key):
        query_strings.append('{}={}'.format(key, queries[key]) if queries[
            key] != '' else key)

    def del_query(key):
        queries.pop(key, None)
    if 'head' in queries:
        add_query('head')
        del_query('head')
    if 'start' in changes:
        add_query('start')
    elif 'start' in queries:
        add_query('start')
    del_query('start')
    if 'limit' in queries:
        add_query('limit')
        del_query('limit')
    for key in sorted(queries):
        add_query(key)
    scheme = cls._get_forwarded(request, 'proto') or request.url.scheme
    host = cls._get_forwarded(request, 'host') or request.host
    forwarded_path = cls._get_forwarded(request, 'path')
    path = path if path is not None else request.path
    query = '?' + '&'.join(query_strings) if query_strings else ''
    url = '{}://{}{}{}{}'.format(scheme, host, forwarded_path, path, query)
    return url