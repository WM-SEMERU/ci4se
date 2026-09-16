def reduce_uri(self, uri, default_port=True):
    parts = urlsplit(uri)
    if parts[1]:
        scheme = parts[0]
        authority = parts[1]
        path = parts[2] or '/'
    else:
        scheme = None
        authority = uri
        path = '/'
    host, port = splitport(authority)
    if default_port and port is None and scheme is not None:
        dport = {'http': 80, 'https': 443}.get(scheme)
        if dport is not None:
            authority = '%s:%d' % (host, dport)
    return authority, path