def _create_stream(self, max_buffer_size, af, addr, **kwargs):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _set_tcp_keepalive(sock, self.opts)
    stream = tornado.iostream.IOStream(sock, max_buffer_size=max_buffer_size)
    if tornado.version_info < (5,):
        return stream.connect(addr)
    return stream, stream.connect(addr)