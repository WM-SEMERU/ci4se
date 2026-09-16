def rollback(self):
    self._check_thread()
    if self.state not in (_STATE_ACTIVE, _STATE_PARTIAL_COMMIT):
        raise TransactionError('Transaction is not active.')
    try:
        if self.state != _STATE_PARTIAL_COMMIT:
            request = transaction_rollback_codec.encode_request(self.id,
                self.thread_id)
            self.client.invoker.invoke_on_connection(request, self.connection
                ).result()
        self.state = _STATE_ROLLED_BACK
    finally:
        self._locals.transaction_exists = False