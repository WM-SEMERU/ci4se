def _connect(self):
    log.debug('Connecting to JLigier')
    self.socket = socket.socket()
    self.socket.connect((self.host, self.port))