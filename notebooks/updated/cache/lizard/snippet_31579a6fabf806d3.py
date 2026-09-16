def get_free_port(ports=None):
    if ports is None:
        with contextlib.closing(socket.socket(socket.AF_INET, socket.
            SOCK_STREAM)) as _socket:
            _socket.bind(('', 0))
            _, port = _socket.getsockname()
            return port
    for port in ports:
        with contextlib.closing(socket.socket(socket.AF_INET, socket.
            SOCK_STREAM)) as _socket:
            try:
                _socket.bind(('', port))
                return port
            except socket.error as ex:
                if ex.errno not in (48, 98):
                    raise
    raise RuntimeError('could not find a free port')