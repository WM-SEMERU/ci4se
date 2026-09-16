def bind_port(requested_port):
    sockets = tornado.netutil.bind_sockets(requested_port)
    if requested_port != 0:
        return sockets, requested_port
    for s in sockets:
        host, port = s.getsockname()[:2]
        if host == '0.0.0.0':
            return sockets, port
    raise RuntimeError('Could not determine the bound port.')