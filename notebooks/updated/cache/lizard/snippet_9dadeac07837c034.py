def handle(self):
    pid, fd = pty.fork()
    if pid:
        protocol = TelnetServerProtocolHandler(self.request, fd)
        protocol.handle()
    else:
        self.execute()