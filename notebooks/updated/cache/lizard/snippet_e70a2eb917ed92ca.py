def server(self):
    server = [s for s in self._server.resources() if s.clientIdentifier ==
        self.machineIdentifier]
    if len(server) == 0:
        raise NotFound('Unable to find server with uuid %s' % self.
            machineIdentifier)
    return server[0]