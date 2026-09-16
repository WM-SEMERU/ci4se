def redirect(self, redirect_error, auth):
    try:
        self.lock()
        _logger.info('Redirecting connection %r.', self.container_id)
        if self.hostname == redirect_error.hostname:
            return
        if self._state != c_uamqp.ConnectionState.END:
            _logger.info('Connection not closed yet - shutting down.')
            self._close()
        self.hostname = redirect_error.hostname
        self.auth = auth
        self._conn = self._create_connection(auth)
        for setting, value in self._settings.items():
            setattr(self, setting, value)
        self._error = None
        self._closing = False
    finally:
        _logger.info('Finished redirecting connection %r.', self.container_id)
        self.release()