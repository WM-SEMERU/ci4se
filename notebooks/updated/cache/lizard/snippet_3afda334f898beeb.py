def parse_query_string(query):
    result = {}
    qparts = query.split('&')
    for item in qparts:
        key, value = item.split('=')
        key = key.strip()
        value = value.strip()
        result[key] = unquote_plus(value)
    return result