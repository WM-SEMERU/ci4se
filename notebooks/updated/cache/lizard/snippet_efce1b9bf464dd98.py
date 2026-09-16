def publish(self, service, routing_id, method, args=None, kwargs=None,
    broadcast=False):
    if not self._peer.up:
        raise errors.Unroutable()
    self._dispatcher.send_proxied_publish(service, routing_id, method, args or
        (), kwargs or {}, singular=not broadcast)