def connect(self, host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    self._reader = sock.makefile(mode='rb')
    self._writer = sock.makefile(mode='wb')