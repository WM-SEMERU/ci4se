def _reset_server(self, address):
    server = self._servers.get(address)
    if server:
        server.reset()
        self._description = self._description.reset_server(address)
        self._update_servers()