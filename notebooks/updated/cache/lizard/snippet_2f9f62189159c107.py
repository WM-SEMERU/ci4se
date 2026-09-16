def connect(self):
    attempt = 0
    for i in self.max_tries_counter:
        attempt += 1
        try:
            self._conn = self._connect()
        except ConnectionError as exc:
            logger.warning(
                'Attempt %s/%s. Connection to %s:%s failed after %sms.',
                attempt, self.max_tries if self.max_tries != 0 else '∞',
                self.host, self.port, self.connection_timeout)
            if attempt == self.max_tries:
                logger.critical('Cannot connect to the Database. Giving up.')
                raise ConnectionError() from exc
        else:
            break