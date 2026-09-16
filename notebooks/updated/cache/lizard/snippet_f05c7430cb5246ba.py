def get_update_clause_from_dict(dictionary, datetime_format='%Y-%m-%d %H:%M:%S'
    ):
    items = []
    CoyoteDb.escape_dictionary(dictionary, datetime_format=datetime_format)
    for k, v in dictionary.iteritems():
        item = '{k} = {v}'.format(k=k, v=v)
        items.append(item)
    clause = ', '.join(item for item in items)
    return clause