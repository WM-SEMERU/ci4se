def get(self):
    return WorkerStatisticsContext(self._version, workspace_sid=self.
        _solution['workspace_sid'], worker_sid=self._solution['worker_sid'])