def bind(self, family, type, proto=0):
    self.socket = sockets.Socket(family, type, proto)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.setblocking(0)
    self.socket.bind(self.bind_addr)