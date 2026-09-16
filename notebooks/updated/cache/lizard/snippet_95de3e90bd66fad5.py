def server_bind(self):
    TCPServer.server_bind(self)
    host, port = self.socket.getsockname()[:2]
    self.server_port = port
    try:
        self.server_name = socket.getfqdn(host)
    except ValueError:
        self.server_name = socket.gethostname()