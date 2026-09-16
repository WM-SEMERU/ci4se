def connect(self, server, port=6667):
    self.socket.connect((server, port))
    self.lines = self._read_lines()
    for event_handler in list(self.on_connect):
        event_handler(self)