def SampleTaskStatus(self, task, status):
    if self._tasks_profiler:
        self._tasks_profiler.Sample(task, status)