def commit_transaction(self):
    with self._transaction_lock:
        local = self._transaction_local
        if not local.pipes:
            raise ValueError('No transaction is currently active.')
        return local.commit()