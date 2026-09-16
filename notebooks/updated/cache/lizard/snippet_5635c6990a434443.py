def listen(self, addr=None):
    self.buffer = buffer.LineBuffer()
    self.handlers = {}
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.passive = True
    default_addr = socket.gethostbyname(socket.gethostname()), 0
    try:
        self.socket.bind(addr or default_addr)
        self.localaddress, self.localport = self.socket.getsockname()
        self.socket.listen(10)
    except socket.error as x:
        raise DCCConnectionError("Couldn't bind socket: %s" % x)
    return self