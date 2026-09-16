def connect(self):
    logger.info('Connecting to RabbitMQ on {broker_url}...'.format(
        broker_url=self.broker_url))
    super(RabbitMQSubscriber, self).connect()
    q = Queue(exchange=self.exchange, exclusive=True, durable=False)
    self.queue = q(self.connection.default_channel)
    self.queue.declare()
    self.thread = Thread(target=self.listen)
    self.thread.setDaemon(True)
    self.thread.start()