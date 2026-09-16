def _get_ssl_sock(self):
    assert self.scheme == 'https', self
    raw_connection = self.url_connection.raw._connection
    if raw_connection.sock is None:
        raw_connection.connect()
    return raw_connection.sock