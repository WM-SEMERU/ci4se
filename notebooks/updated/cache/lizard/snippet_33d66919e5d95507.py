def port(self):
    if 'port' not in self.state:
        sock = socket.socket()
        sock.bind(('', self.requested_port))
        self.state['port'] = sock.getsockname()[1]
        sock.close()
    return self.state['port']