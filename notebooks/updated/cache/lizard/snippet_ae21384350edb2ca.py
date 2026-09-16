def _setup_transport(self):
    if HAVE_PY26_SSL:
        if hasattr(self, 'sslopts'):
            self.sslobj = ssl.wrap_socket(self.sock, **self.sslopts)
        else:
            self.sslobj = ssl.wrap_socket(self.sock)
        self.sslobj.do_handshake()
    else:
        self.sslobj = socket.ssl(self.sock)