def handle(self, connection_id, message_content):
    LOGGER.warning('Received AuthorizationViolation from %s', connection_id)
    endpoint = self._network.connection_id_to_endpoint(connection_id)
    self._network.remove_connection(connection_id)
    self._gossip.remove_temp_endpoint(endpoint)
    return HandlerResult(HandlerStatus.DROP)