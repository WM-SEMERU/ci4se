def server_sends_binary(self, message, name=None, connection=None, label=None):
    server, name = self._servers.get_with_name(name)
    server.send(message, alias=connection)
    self._register_send(server, label, name, connection=connection)