def in_transaction(self):
    self._in_transaction = self._in_transaction and self.is_connected
    return self._in_transaction