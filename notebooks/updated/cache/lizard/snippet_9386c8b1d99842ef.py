def allocate_tcp_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if platformType == 'posix' and sys.platform != 'cygwin':
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 0))
    port = s.getsockname()[1]
    s.close()
    return port