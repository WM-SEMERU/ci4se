def on_queue_declareok(self, method_frame):
    _logger.info('Binding %s to %s with %s', self.EXCHANGE, self._queue,
        self._routing_key)
    self._channel.queue_bind(self.on_bindok, self._queue, self.EXCHANGE,
        self._routing_key)