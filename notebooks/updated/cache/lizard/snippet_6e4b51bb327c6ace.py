def _escape_query(self, query, escaped=False):
    if escaped:
        return query
    query = six.text_type(query)
    for e in ['+', '-', '&&', '||', '!', '(', ')', '{', '}', '[', ']', '^',
        '"', '~', '*', '?', ':', ' ']:
        query = query.replace(e, '\\%s' % e)
    return query