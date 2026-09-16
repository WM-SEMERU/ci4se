def date_parse(s):
    s = as_str(s)
    if s.endswith(' BC'):
        raise errors.NotSupportedError(
            'Dates Before Christ are not supported. Got: {0}'.format(s))
    return date(*map(lambda x: min(int(x), 9999), s.split('-')))