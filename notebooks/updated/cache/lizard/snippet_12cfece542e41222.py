def connect(self, host='localhost'):
    get_logger().info('Connecting to RabbitMQ server...')
    self._conn = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    self._channel = self._conn.channel()
    get_logger().info('Declaring topic exchanger {}...'.format(self.exchange))
    self._channel.exchange_declare(exchange=self.exchange, type='topic')
    get_logger().info('Creating RabbitMQ queue...')
    result = self._channel.queue_declare(exclusive=True)
    self._queue_name = result.method.queue
    if self.listen_all:
        get_logger().info('Binding queue to exchanger {} (listen all)...'.
            format(self.exchange))
        self._channel.queue_bind(exchange=self.exchange, queue=self.
            _queue_name, routing_key='*')
    else:
        for routing_key in self.topics:
            get_logger().info(
                'Binding queue to exchanger {} with routing key {}...'.
                format(self.exchange, routing_key))
            self._channel.queue_bind(exchange=self.exchange, queue=self.
                _queue_name, routing_key=routing_key)
    get_logger().info('Binding callback...')
    self._channel.basic_consume(self._callback, queue=self._queue_name,
        no_ack=True)