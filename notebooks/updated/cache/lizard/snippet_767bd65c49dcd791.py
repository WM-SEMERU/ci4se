def _parse_dsn(dsn):
    conn_params = urlparse(dsn)
    init_args = {}
    scheme_info = conn_params.scheme.split('+')
    if len(scheme_info) == 1:
        scheme = scheme_info[0]
        modifier = None
    else:
        modifier, scheme = scheme_info
    if scheme != 'influxdb':
        raise ValueError('Unknown scheme "{0}".'.format(scheme))
    if modifier:
        if modifier == 'udp':
            init_args['use_udp'] = True
        elif modifier == 'https':
            init_args['ssl'] = True
        else:
            raise ValueError('Unknown modifier "{0}".'.format(modifier))
    netlocs = conn_params.netloc.split(',')
    init_args['hosts'] = []
    for netloc in netlocs:
        parsed = _parse_netloc(netloc)
        init_args['hosts'].append((parsed['host'], int(parsed['port'])))
        init_args['username'] = parsed['username']
        init_args['password'] = parsed['password']
    if conn_params.path and len(conn_params.path) > 1:
        init_args['database'] = conn_params.path[1:]
    return init_args