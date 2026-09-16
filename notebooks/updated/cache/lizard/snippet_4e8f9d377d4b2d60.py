def get_socket(self):
    import eventlet
    socket_args = {}
    for arg in ('backlog', 'family'):
        try:
            socket_args[arg] = self.options.pop(arg)
        except KeyError:
            pass
    ssl_args = {}
    for arg in ('keyfile', 'certfile', 'server_side', 'cert_reqs',
        'ssl_version', 'ca_certs', 'do_handshake_on_connect',
        'suppress_ragged_eofs', 'ciphers'):
        try:
            ssl_args[arg] = self.options.pop(arg)
        except KeyError:
            pass
    address = self.host, self.port
    try:
        sock = eventlet.listen(address, **socket_args)
    except TypeError:
        sock = eventlet.listen(address)
    if ssl_args:
        sock = eventlet.wrap_ssl(sock, **ssl_args)
    return sock