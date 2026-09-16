def connection_made(self, transport):
    self.transport = transport
    sock = self.transport.get_extra_info('socket')
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    self.loop.call_soon(self.discover)