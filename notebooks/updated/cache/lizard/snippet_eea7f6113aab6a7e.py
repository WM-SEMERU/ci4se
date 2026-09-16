def _get_brokerclient(self, node_id):
    if self._closing:
        raise ClientError(
            'Cannot get broker client for node_id={}: {} has been closed'.
            format(node_id, self))
    if node_id not in self.clients:
        broker_metadata = self._brokers[node_id]
        log.debug('%r: creating client for %s', self, broker_metadata)
        self.clients[node_id] = _KafkaBrokerClient(self.reactor, self.
            _endpoint_factory, broker_metadata, self.clientId, self.
            _retry_policy)
    return self.clients[node_id]