def _proxy(self):
    if self._context is None:
        self._context = WorkerStatisticsContext(self._version,
            workspace_sid=self._solution['workspace_sid'], worker_sid=self.
            _solution['worker_sid'])
    return self._context