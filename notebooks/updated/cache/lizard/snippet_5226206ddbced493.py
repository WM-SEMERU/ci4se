def add_tcp_callback(self, port, callback, threaded_callback=False):
    if not callback:
        raise AttributeError('No callback')
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind((_TCP_SOCKET_HOST, port))
    serversocket.listen(1)
    serversocket.setblocking(0)
    self._epoll.register(serversocket.fileno(), select.EPOLLIN)
    cb = callback if not threaded_callback else partial(_threaded_callback,
        callback)
    self._tcp_server_sockets[serversocket.fileno()] = serversocket, cb
    debug('Socket server started at port %s and callback added.' % port)