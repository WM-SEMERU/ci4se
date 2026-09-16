def commit(self):
    if self._transaction_nesting_level == 0:
        raise DBALConnectionError.no_active_transaction()
    if self._is_rollback_only:
        raise DBALConnectionError.commit_failed_rollback_only()
    self.ensure_connected()
    if self._transaction_nesting_level == 1:
        self._driver.commit()
    elif self._nest_transactions_with_savepoints:
        self.release_savepoint(self._get_nested_transaction_savepoint_name())
    self._transaction_nesting_level -= 1
    if not self._auto_commit and self._transaction_nesting_level == 0:
        self.begin_transaction()