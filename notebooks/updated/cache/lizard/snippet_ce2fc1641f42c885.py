def _proxy(self):
    if self._context is None:
        self._context = ExecutionContext(self._version, flow_sid=self.
            _solution['flow_sid'], sid=self._solution['sid'])
    return self._context