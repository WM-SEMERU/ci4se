def remove_tcp_port(self, port):
    if port in self._used_tcp_ports:
        self._used_tcp_ports.remove(port)