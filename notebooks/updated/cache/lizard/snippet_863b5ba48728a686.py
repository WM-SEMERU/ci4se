def setup_exchange(self, exchange_name):
    self._logger.debug('Declaring exchange %s' % exchange_name)
    try:
        self._channel.exchange_declare(self.on_exchange_declareok,
            exchange_name, self._exchange_type)
    except Exception as e:
        self._logger.exception(e)