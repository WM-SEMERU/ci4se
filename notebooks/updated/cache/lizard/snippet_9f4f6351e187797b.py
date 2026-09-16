def url(self):
    scheme = self.environ.get('wsgi.url_scheme', 'http')
    host = self.environ.get('HTTP_X_FORWARDED_HOST', self.environ.get(
        'HTTP_HOST', None))
    if not host:
        host = self.environ.get('SERVER_NAME')
        port = self.environ.get('SERVER_PORT', '80')
        if scheme + port not in ('https443', 'http80'):
            host += ':' + port
    parts = scheme, host, urlquote(self.fullpath), self.query_string, ''
    return urlunsplit(parts)