def send(self, request_id, payload):
    log.debug('About to send %d bytes to Kafka, request %d' % (len(payload),
        request_id))
    if not self._sock:
        self.reinit()
    try:
        self._sock.sendall(payload)
    except socket.error:
        log.exception('Unable to send payload to Kafka')
        self._raise_connection_error()