def close(self):
    with self._lock:
        for server in self._servers.values():
            server.close()
        self._description = self._description.reset()
        self._update_servers()
        self._opened = False
    if self._publish_tp:
        self._events.put((self._listeners.publish_topology_closed, (self.
            _topology_id,)))
    if self._publish_server or self._publish_tp:
        self.__events_executor.close()