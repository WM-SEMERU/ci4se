async def connect(self):
    if self.connected or self.is_connecting:
        return
    self._is_connecting = True
    try:
        logger.info('Connecting to RabbitMQ...')
        self._transport, self._protocol = await aioamqp.connect(**self.
            _connection_parameters)
        logger.info('Getting channel...')
        self._channel = await self._protocol.channel()
        if self._global_qos is not None:
            logger.info('Setting prefetch count on connection (%s)', self.
                _global_qos)
            await self._channel.basic_qos(0, self._global_qos, 1)
        logger.info("Connecting to exchange '%s (%s)'", self._exchange_name,
            self._exchange_type)
        await self._channel.exchange(self._exchange_name, self._exchange_type)
    except (aioamqp.AmqpClosedConnection, Exception):
        logger.error('Error initializing RabbitMQ connection', exc_info=True)
        self._is_connecting = False
        raise exceptions.StreamConnectionError
    self._is_connecting = False