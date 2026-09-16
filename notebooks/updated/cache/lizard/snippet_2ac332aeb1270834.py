def term_from_uri(uri):
    if uri is None:
        return None
    if isinstance(uri, rdflib.Literal):
        uri = str(uri.toPython())
    patterns = ['http://www.openbel.org/bel/namespace//(.*)',
        'http://www.openbel.org/vocabulary//(.*)',
        'http://www.openbel.org/bel//(.*)',
        'http://www.openbel.org/bel/namespace/(.*)',
        'http://www.openbel.org/vocabulary/(.*)',
        'http://www.openbel.org/bel/(.*)']
    for pr in patterns:
        match = re.match(pr, uri)
        if match is not None:
            term = match.groups()[0]
            term = unquote(term)
            return term
    return uri