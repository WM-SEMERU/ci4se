def close(self):
    if self._socket is not None and self._conn is not None:
        message_input = UnityMessage()
        message_input.header.status = 400
        self._communicator_send(message_input.SerializeToString())
    if self._socket is not None:
        self._socket.close()
        self._socket = None
    if self._socket is not None:
        self._conn.close()
        self._conn = None