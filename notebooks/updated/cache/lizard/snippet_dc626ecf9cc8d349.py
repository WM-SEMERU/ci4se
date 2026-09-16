def filter(resources, query):
    if '{' in query:
        query, _ = query.split('{')
        logger.warning(
            'optional part of the query expression not supported. See filter2')
    try:
        query = query.replace('?', '.')
        matcher = re.compile(query, re.IGNORECASE)
    except re.error:
        raise errors.VisaIOError(constants.VI_ERROR_INV_EXPR)
    return tuple(res for res in resources if matcher.match(res))