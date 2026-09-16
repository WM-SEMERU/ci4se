def run(self):
    try:
        for index, port in enumerate(self.possible_ports):
            try:
                self.httpd = self._create_server(port)
            except socket.error as e:
                if index + 1 < len(self.possible_ports
                    ) and e.error == errno.EADDRINUSE:
                    continue
                else:
                    raise
            else:
                self.port = port
                break
        self.is_ready.set()
        self.httpd.serve_forever()
    except Exception as e:
        self.error = e
        self.is_ready.set()