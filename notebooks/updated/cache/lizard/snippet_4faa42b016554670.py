def validate_url(self, url):
    url_path = to_bytes_safe(url.path)
    url_path = urllib.parse.quote(url_path, safe=b'/%')
    url_query = to_bytes_safe(url.query)
    url_query = urllib.parse.quote(url_query, safe=b'?=&')
    url = urllib.parse.ParseResult(url.scheme, url.netloc, url_path, url.
        params, url_query, url.fragment)
    has_hostname = url.hostname is not None and len(url.hostname) > 0
    has_http_scheme = url.scheme in ('http', 'https')
    has_path = not len(url.path) or url.path.startswith('/')
    if not (has_hostname and has_http_scheme and has_path):
        raise NotSupported('invalid url: %s' % repr(url))
    return url