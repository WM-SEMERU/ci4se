def on_stop(self):
    LOGGER.debug('rabbitmq.Requester.on_stop')
    try:
        self.channel.close()
    except Exception as e:
        LOGGER.warn(
            'rabbitmq.Requester.on_stop - Exception raised while closing channel'
            )
    try:
        self.connection.close()
    except Exception as e:
        LOGGER.warn(
            'rabbitmq.Requester.on_stop - Exception raised while closing connection'
            )