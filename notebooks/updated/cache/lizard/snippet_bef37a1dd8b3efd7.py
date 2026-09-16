def _send(self, key, value, metric_type):
    try:
        payload = self._build_payload(key, value, metric_type)
        LOGGER.debug('Sending statsd payload: %r', payload)
        self._socket.sendto(payload.encode('utf-8'), self._address)
    except socket.error:
        LOGGER.exception('Error sending statsd metric')