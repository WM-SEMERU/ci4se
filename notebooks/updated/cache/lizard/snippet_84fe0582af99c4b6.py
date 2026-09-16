def connection_made(self, transport):
    self.logger.info('Connection made at object %s', id(self))
    self.transport = transport
    self.keepalive = True
    if self._timeout:
        self.logger.debug('Registering timeout event')
        self._timout_handle = self._loop.call_later(self._timeout, self.
            _handle_timeout)