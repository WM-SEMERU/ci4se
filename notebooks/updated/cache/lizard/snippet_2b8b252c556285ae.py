def server_bind(self):
    TCPServer.server_bind(self)
    _, self.server_port = self.socket.getsockname()[:2]