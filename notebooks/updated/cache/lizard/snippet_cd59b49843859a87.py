def stop_consuming(self):
    if self._channel:
        logger.info('Sending a Basic.Cancel RPC command to RabbitMQ')
        self._channel.basic_cancel(self.on_cancelok, self._consumer_tag)