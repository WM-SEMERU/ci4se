def on_ping(self, data):
    self.log.debug('jupyter_server_proxy: on_ping: {}'.format(data))
    self._record_activity()
    if hasattr(self, 'ws'):
        self.ws.protocol.write_ping(data)