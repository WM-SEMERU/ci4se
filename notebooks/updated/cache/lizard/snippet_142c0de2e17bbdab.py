def cherrypy_server_runner(app, global_conf=None, host='127.0.0.1', port=
    None, ssl_pem=None, protocol_version=None, numthreads=None, server_name
    =None, max=None, request_queue_size=None, timeout=None):
    is_ssl = False
    if ssl_pem:
        port = port or 4443
        is_ssl = True
    if not port:
        if ':' in host:
            host, port = host.split(':', 1)
        else:
            port = 8080
    bind_addr = host, int(port)
    kwargs = {}
    for var_name in ('numthreads', 'max', 'request_queue_size', 'timeout'):
        var = locals()[var_name]
        if var is not None:
            kwargs[var_name] = int(var)
    server = None
    try:
        import cheroot.wsgi as wsgiserver
        server = wsgiserver.Server(bind_addr, app, server_name=server_name,
            **kwargs)
    except ImportError:
        from cherrypy import wsgiserver
        server = wsgiserver.CherryPyWSGIServer(bind_addr, app, server_name=
            server_name, **kwargs)
    server.ssl_certificate = server.ssl_private_key = ssl_pem
    if protocol_version:
        server.protocol = protocol_version
    try:
        protocol = is_ssl and 'https' or 'http'
        if host == '0.0.0.0':
            print('serving on 0.0.0.0:%s view at %s://127.0.0.1:%s' % (port,
                protocol, port))
        else:
            print('serving on %s://%s:%s' % (protocol, host, port))
        server.start()
    except (KeyboardInterrupt, SystemExit):
        server.stop()
    return server