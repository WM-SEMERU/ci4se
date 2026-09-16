def _republish_dropped_message(self, reason):
    self.logger.debug('Republishing due to ProcessingException')
    properties = dict(self._message.properties) or {}
    if 'headers' not in properties or not properties['headers']:
        properties['headers'] = {}
    properties['headers']['X-Dropped-By'] = self.name
    properties['headers']['X-Dropped-Reason'] = reason
    properties['headers']['X-Dropped-Timestamp'] = datetime.datetime.utcnow(
        ).isoformat()
    properties['headers']['X-Original-Exchange'] = self._message.exchange
    self._message.channel.basic_publish(self._drop_exchange, self._message.
        routing_key, self._message.body, pika.BasicProperties(**properties))