def setup_exchange(self):
    logger.debug('Declaring exchange %s', self._exchange)
    self._channel.exchange_declare(self.on_exchange_declareok, self.
        _exchange, self._exchange_type, durable=True)