def send(self, message):
    if not message or not self.protocol or not self.protocol.transport:
        return
    if not self.can_log:
        _LOGGER.debug('Sending %s', message.strip())
    try:
        self.protocol.transport.write(message.encode())
    except OSError as exc:
        _LOGGER.error('Failed writing to transport %s: %s', self.protocol.
            transport, exc)
        self.protocol.transport.close()
        self.protocol.conn_lost_callback()