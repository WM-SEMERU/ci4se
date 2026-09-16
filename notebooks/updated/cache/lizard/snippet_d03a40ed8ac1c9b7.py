def _create_http_basic_session(self, username, password, timeout=None):
    verify = self._options['verify']
    self._session = ResilientSession(timeout=timeout)
    self._session.verify = verify
    self._session.auth = username, password
    self._session.cert = self._options['client_cert']