def SetServerInformation(self, server, port):
    self._host = server
    self._port = port
    logger.debug('Elasticsearch server: {0!s} port: {1:d}'.format(server, port)
        )