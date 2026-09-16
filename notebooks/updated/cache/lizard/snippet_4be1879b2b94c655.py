def connect(self):
    if self._sock:
        return
    try:
        sock = self._connect()
    except socket.error:
        e = sys.exc_info()[1]
        raise ConnectionError(self._error_message(e))
    self._sock = sock
    try:
        self.on_connect()
    except SSDBError:
        self.disconnect()
        raise
    for callback in self._connect_callbacks:
        callback(self)