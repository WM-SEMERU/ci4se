def send_datagram(self, message):
    host, port = message.destination
    logger.debug('send_datagram - ' + str(message))
    serializer = Serializer()
    raw_message = serializer.serialize(message)
    try:
        self._socket.sendto(raw_message, (host, port))
    except Exception as e:
        if self._cb_ignore_write_exception is not None and isinstance(self.
            _cb_ignore_write_exception, collections.Callable):
            if not self._cb_ignore_write_exception(e, self):
                raise
    for opt in message.options:
        if opt.number == defines.OptionRegistry.NO_RESPONSE.number:
            if opt.value == 26:
                return
    if self._receiver_thread is None or not self._receiver_thread.isAlive():
        self._receiver_thread = threading.Thread(target=self.receive_datagram)
        self._receiver_thread.daemon = True
        self._receiver_thread.start()