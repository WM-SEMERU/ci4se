def _consume_add_and_get_tag(self, consume_rpc_result):
    consumer_tag = consume_rpc_result['consumer_tag']
    self._channel.add_consumer_tag(consumer_tag)
    return consumer_tag