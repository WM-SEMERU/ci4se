def _authority(scheme=DEFAULT_SCHEME, host=DEFAULT_HOST, port=DEFAULT_PORT):
    if ':' in host:
        host = '[' + host + ']'
    return UrlEncoded('%s://%s:%s' % (scheme, host, port), skip_encode=True)