def refresh(self):
    key = '%s/refresh' % self.key
    self._server.query(key, method=self._server._session.put)