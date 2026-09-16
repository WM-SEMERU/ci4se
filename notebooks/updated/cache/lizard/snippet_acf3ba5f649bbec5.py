def local_connect_and_auth(port, auth_secret):
    sock = None
    errors = []
    for res in socket.getaddrinfo('127.0.0.1', port, socket.AF_UNSPEC,
        socket.SOCK_STREAM):
        af, socktype, proto, _, sa = res
        try:
            sock = socket.socket(af, socktype, proto)
            sock.settimeout(15)
            sock.connect(sa)
            sockfile = sock.makefile('rwb', 65536)
            _do_server_auth(sockfile, auth_secret)
            return sockfile, sock
        except socket.error as e:
            emsg = _exception_message(e)
            errors.append(
                'tried to connect to %s, but an error occured: %s' % (sa, emsg)
                )
            sock.close()
            sock = None
    raise Exception('could not open socket: %s' % errors)