def makeSocket(self, timeout=1):
    plain_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if hasattr(plain_socket, 'settimeout'):
        plain_socket.settimeout(timeout)
    wrapped_socket = ssl.wrap_socket(plain_socket, ca_certs=self.ca_certs,
        cert_reqs=self.reqs, keyfile=self.keyfile, certfile=self.certfile)
    wrapped_socket.connect((self.host, self.port))
    return wrapped_socket