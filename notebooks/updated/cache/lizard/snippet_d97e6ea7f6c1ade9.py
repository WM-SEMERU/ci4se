def start(self):
    if self.is_alive:
        self.logger.warning('Already started!')
        return
    self._create_tunnels()
    if not self.is_active:
        self._raise(BaseSSHTunnelForwarderError, reason=
            'Could not establish session to SSH gateway')
    for _srv in self._server_list:
        thread = threading.Thread(target=self._serve_forever_wrapper, args=
            (_srv,), name='Srv-{0}'.format(address_to_str(_srv.local_port)))
        thread.daemon = self.daemon_forward_servers
        thread.start()
        self._check_tunnel(_srv)
    self.is_alive = any(self.tunnel_is_up.values())
    if not self.is_alive:
        self._raise(HandlerSSHTunnelForwarderError,
            'An error occurred while opening tunnels.')