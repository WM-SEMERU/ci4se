def set_tunnel(self, tunnel_type, tunnel, callback=None):
    orig_tunnel = self.tunnels.get(tunnel_type, (None, None))[0]
    if orig_tunnel is not None:
        _logger.debug('Unsubscribe: %s', (orig_tunnel,))
        self.client.unsubscribe(str(orig_tunnel))
    self.tunnels[tunnel_type] = tunnel, callback
    if callback is not None:
        self.message_callback_add(tunnel, callback)
    self.client.subscribe(str(tunnel))
    _logger.debug('Subscribe: %s', (tunnel,))