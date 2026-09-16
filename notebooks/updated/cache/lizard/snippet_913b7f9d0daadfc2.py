def _on_scan_request(self, sequence, topic, message):
    if messages.ProbeCommand.matches(message):
        self._logger.debug('Received probe message on topic %s, message=%s',
            topic, message)
        self._loop.add_callback(self._publish_scan_response, message['client'])
    else:
        self._logger.warn('Invalid message received on topic %s, message=%s',
            topic, message)