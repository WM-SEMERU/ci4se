def reset_rammbock(self):
    for client in self._clients:
        client.close()
    for server in self._servers:
        server.close()
    self._init_caches()