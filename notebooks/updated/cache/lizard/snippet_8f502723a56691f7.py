def _set_socket_timeout(cls, sock, timeout=None):
    if timeout is not None:
        prev_timeout = sock.gettimeout()
    try:
        if timeout is not None:
            sock.settimeout(timeout)
        yield
    except socket.timeout:
        raise cls.ProcessStreamTimeout('socket read timed out with timeout {}'
            .format(timeout))
    finally:
        if timeout is not None:
            sock.settimeout(prev_timeout)