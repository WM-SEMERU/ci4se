def _uri_split(uri):
    scheme, netloc, path, query, fragment = _safe_urlsplit(uri)
    auth = None
    port = None
    if '@' in netloc:
        auth, netloc = netloc.split('@', 1)
    if netloc.startswith('['):
        host, port_part = netloc[1:].split(']', 1)
        if port_part.startswith(':'):
            port = port_part[1:]
    elif ':' in netloc:
        host, port = netloc.split(':', 1)
    else:
        host = netloc
    return scheme, auth, host, port, path, query, fragment