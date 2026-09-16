def clientConnectionFailed(self, connector, reason):
    log.debug('Connect failed: %s', reason)
    self.conn.defunct(reason.value)