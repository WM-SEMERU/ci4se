def send_message(self, msg, connection_id=None):
    zmq_identity = None
    if connection_id is not None and self._connections is not None:
        if connection_id in self._connections:
            connection_info = self._connections.get(connection_id)
            if connection_info.connection_type == ConnectionType.ZMQ_IDENTITY:
                zmq_identity = connection_info.connection
        else:
            LOGGER.debug("Can't send to %s, not in self._connections",
                connection_id)
    self._ready.wait()
    if zmq_identity is None:
        message_bundle = [msg.SerializeToString()]
    else:
        message_bundle = [bytes(zmq_identity), msg.SerializeToString()]
    try:
        asyncio.run_coroutine_threadsafe(self._send_message_frame(
            message_bundle), self._event_loop)
    except RuntimeError:
        pass