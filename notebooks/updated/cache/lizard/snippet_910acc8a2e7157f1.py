def url_to_parts(url):
    if not url:
        return None
    scheme, netloc, path, query, fragment = _urlsplit(url)
    if not path or path == '/':
        path = []
    else:
        path = path.strip('/').split('/')
    if not query:
        query = {}
    else:
        query = _parse_qs(query)
    return _urllib_parse.SplitResult(scheme, netloc, path, query, fragment)