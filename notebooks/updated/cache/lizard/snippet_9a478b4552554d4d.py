def send_last_message(self, msg, connection_id=None):
    zmq_identity = None
    if connection_id is not None and self._connections is not None:
        if connection_id in self._connections:
            connection_info = self._connections.get(connection_id)
            if connection_info.connection_type == ConnectionType.ZMQ_IDENTITY:
                zmq_identity = connection_info.connection
            del self._connections[connection_id]
        else:
            LOGGER.debug("Can't send to %s, not in self._connections",
                connection_id)
            return
    self._ready.wait()
    try:
        asyncio.run_coroutine_threadsafe(self._send_last_message(
            zmq_identity, msg), self._event_loop)
    except RuntimeError:
        pass