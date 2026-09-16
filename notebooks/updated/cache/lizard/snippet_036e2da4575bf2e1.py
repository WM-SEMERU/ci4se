def process(self, metric):
    for rmq_server in self.connections.keys():
        try:
            if self.connections[rmq_server] is None or self.connections[
                rmq_server].is_open is False:
                self._bind(rmq_server)
            channel = self.channels[rmq_server]
            channel.basic_publish(exchange=self.rmq_exchange, routing_key=
                '', body='%s' % metric)
        except Exception as exception:
            self.log.error('Failed publishing to %s, attempting reconnect',
                rmq_server)
            self.log.debug('Caught exception: %s', exception)
            self._unbind(rmq_server)
            self._bind(rmq_server)