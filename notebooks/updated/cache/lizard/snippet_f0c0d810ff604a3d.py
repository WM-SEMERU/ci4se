def get_transaction(self, clear=False):
    transaction = getattr(self.thread_local, 'transaction', None)
    if clear:
        self.thread_local.transaction = None
    return transaction