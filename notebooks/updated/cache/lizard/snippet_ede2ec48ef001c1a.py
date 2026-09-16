def parse_ctype(ctype):
    result_ctype = None
    result = {}
    for part in quoted_split(ctype, ';'):
        if result_ctype is None:
            result_ctype = part
            result['_'] = part
            continue
        equal = part.find('=')
        if equal > 0 and part.find('"', 0, equal) < 0:
            result[part[:equal]] = unquote(part[equal + 1:])
        else:
            result[part] = True
    if result_ctype is None:
        result_ctype = ''
    return result_ctype, result