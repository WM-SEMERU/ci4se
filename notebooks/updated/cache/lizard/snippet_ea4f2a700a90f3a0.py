def _send(self, data):
    try:
        self._sock.sendto(data.encode('ascii'), self._addr)
    except (socket.error, RuntimeError):
        pass