def release(self, connection):
    self._checkpid()
    if connection.pid == self.pid:
        idx = connection._pattern_idx
        self._in_use_connections[idx].remove(connection)
        self._available_connections[idx].append(connection)