def disconnect(self):
    self._parser.on_disconnect()
    if self._sock is None:
        return
    try:
        self._sock.shutdown(socket.SHUT_RDWR)
        self._sock.close()
    except socket.error:
        pass
    self._sock = None