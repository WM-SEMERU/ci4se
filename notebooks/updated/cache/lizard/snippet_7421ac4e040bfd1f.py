def _parse_uri_options(self, parsed_uri, use_ssl=False, ssl_options=None):
    ssl_options = ssl_options or {}
    kwargs = urlparse.parse_qs(parsed_uri.query)
    vhost = urlparse.unquote(parsed_uri.path[1:]) or DEFAULT_VIRTUAL_HOST
    options = {'ssl': use_ssl, 'virtual_host': vhost, 'heartbeat': int(
        kwargs.pop('heartbeat', [DEFAULT_HEARTBEAT_INTERVAL])[0]),
        'timeout': int(kwargs.pop('timeout', [DEFAULT_SOCKET_TIMEOUT])[0])}
    if use_ssl:
        if not compatibility.SSL_SUPPORTED:
            raise AMQPConnectionError(
                'Python not compiled with support for TLSv1 or higher')
        ssl_options.update(self._parse_ssl_options(kwargs))
        options['ssl_options'] = ssl_options
    return options