def get_url(path, host, port, method='http'):
    return urlunsplit((method, '%s:%s' % (host, port), path, '', ''))