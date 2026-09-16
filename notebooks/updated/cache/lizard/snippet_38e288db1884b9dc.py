def store_traces(self, value):
    if not value:
        self.logger.debug('Stopping storing received lines for dut %d',
            self.index)
        self._store_traces = False
    else:
        self.logger.debug('Resuming storing received lines for dut %d',
            self.index)
        self._store_traces = True