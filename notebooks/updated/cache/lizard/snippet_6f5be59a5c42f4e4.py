def free(self, connection):
    LOGGER.debug('Pool %s freeing connection %s', self.id, id(connection))
    try:
        self.connection_handle(connection).free()
    except KeyError:
        raise ConnectionNotFoundError(self.id, id(connection))
    if self.idle_connections == list(self.connections.values()):
        with self._lock:
            self.idle_start = self.time_method()
    LOGGER.debug('Pool %s freed connection %s', self.id, id(connection))