def accept_connection(self, name=None, alias=None, timeout=0):
    server = self._servers.get(name)
    server.accept_connection(alias, timeout)