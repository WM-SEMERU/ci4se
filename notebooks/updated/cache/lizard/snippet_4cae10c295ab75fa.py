def commit(self):
    self._check_thread()
    if self.state != _STATE_ACTIVE:
        raise TransactionError('Transaction is not active.')
    try:
        self._check_timeout()
        request = transaction_commit_codec.encode_request(self.id, self.
            thread_id)
        self.client.invoker.invoke_on_connection(request, self.connection
            ).result()
        self.state = _STATE_COMMITTED
    except:
        self.state = _STATE_PARTIAL_COMMIT
        raise
    finally:
        self._locals.transaction_exists = False