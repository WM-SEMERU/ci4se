def GetProcessedTaskByIdentifier(self, task_identifier):
    with self._lock:
        task = self._tasks_processing.get(task_identifier, None)
        if not task:
            task = self._tasks_queued.get(task_identifier, None)
        if not task:
            task = self._tasks_abandoned.get(task_identifier, None)
        if not task:
            raise KeyError('Status of task {0:s} is unknown'.format(
                task_identifier))
    return task