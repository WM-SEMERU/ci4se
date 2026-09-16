def close(self):
    from neobolt.exceptions import ConnectionExpired, CypherError, ServiceUnavailable
    try:
        if self.has_transaction():
            try:
                self.rollback_transaction()
            except (CypherError, TransactionError, SessionError,
                ConnectionExpired, ServiceUnavailable):
                pass
    finally:
        self._closed = True
    self._disconnect(sync=True)