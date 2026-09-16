def incr(self, key, value):
    server = self._get_server(key)
    return server.incr(key, value)