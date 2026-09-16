def steps(self):
    if self._steps is None:
        self._steps = ExecutionStepList(self._version, flow_sid=self.
            _solution['flow_sid'], execution_sid=self._solution['sid'])
    return self._steps