def urisplit(uri):
    inner_part = re.compile('\\(\\(.*?\\)\\)')
    m = inner_part.search(uri)
    inner_value = ''
    if m is not None:
        inner_value = uri[m.start():m.end()]
        uri = uri[:m.start()] + '__inner_part__' + uri[m.end():]
    regex = '^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\\?([^#]*))?(#(.*))?'
    p = re.match(regex, uri).groups()
    scheme, authority, path, query, fragment = p[1], p[3], p[4], p[6], p[8]
    authority = authority.replace('__inner_part__', inner_value)
    if authority == '.':
        path = ''.join([authority, path])
        authority = None
    if scheme not in ['http', 'https']:
        if fragment:
            path = '#'.join([path, fragment])
            fragment = ''
    return scheme, authority, path, query, fragment