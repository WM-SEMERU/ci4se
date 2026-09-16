def _parse_wsgi_headers(wsgi_environ):
    prefix = 'HTTP_'
    p_len = len(prefix)
    headers = {key[p_len:].replace('_', '-').lower(): val for key, val in
        wsgi_environ.items() if key.startswith(prefix)}
    return headers