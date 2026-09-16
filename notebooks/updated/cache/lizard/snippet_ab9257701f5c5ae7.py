def connect(self):
    try:
        self.telnet = Telnet(self.host, self.port)
        time.sleep(1)
        self.get()
        self.get('login admin admin')
        self.update()
    except socket.gaierror:
        self.telnet = None
        LOGGER.error('Cannot connect to %s (%d)', self.host, self.retries)