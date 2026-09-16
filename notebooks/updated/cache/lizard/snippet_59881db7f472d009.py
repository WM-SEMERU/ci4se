def rollback_savepoint(self, savepoint):
    if not self._platform.is_savepoints_supported():
        raise DBALConnectionError.savepoints_not_supported()
    self.ensure_connected()
    self._platform.rollback_savepoint(savepoint)