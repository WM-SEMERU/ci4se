def handle_read(self):
    while True:
        try:
            c = self.recv(1)
        except socket.error as e:
            if e.errno == errno.EWOULDBLOCK:
                return
            else:
                raise
        else:
            self._do(c)
            self.socket.setblocking(True)
            self.send(b'A')
            self.socket.setblocking(False)