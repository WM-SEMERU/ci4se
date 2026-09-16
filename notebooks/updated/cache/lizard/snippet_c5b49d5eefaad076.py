def url_join(base, *args):
    scheme, netloc, path, query, fragment = urlsplit(base)
    path = path if len(path) else '/'
    path = posixpath.join(path, *[('%s' % x) for x in args])
    return urlunsplit([scheme, netloc, path, query, fragment])