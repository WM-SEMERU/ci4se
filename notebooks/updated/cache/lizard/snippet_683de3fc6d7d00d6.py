def fetch_next_block(self):
    if self._ex_context is None:
        self._ex_context = self._create_execution_context()
    return self._ex_context.fetch_next_block()