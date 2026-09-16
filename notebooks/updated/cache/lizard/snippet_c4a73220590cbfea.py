def run(self):
    self.protocol = self.protocol_factory()
    try:
        self.protocol.connection_made(self)
    except Exception as exc:
        self.alive = False
        self.protocol.connection_lost(exc)
        self._connection_made.set()
        return
    error = None
    self._connection_made.set()
    while self.alive:
        data = None
        try:
            available_socks = self._check_socket()
            if available_socks[0]:
                data = self.sock.recv(120)
        except Exception as exc:
            error = exc
            break
        else:
            if data:
                try:
                    self.protocol.data_received(data)
                except Exception as exc:
                    error = exc
                    break
        try:
            self._check_connection()
        except OSError as exc:
            error = exc
            break
        time.sleep(0.02)
    self.alive = False
    self.protocol.connection_lost(error)
    self.protocol = None