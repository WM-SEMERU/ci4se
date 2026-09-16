def stop(self, wait=True):
    for context in self._applications.values():
        context.run_unload_hook()
    self._stats_job.stop()
    if self._mem_job is not None:
        self._mem_job.stop()
    self._cleanup_job.stop()
    if self._ping_job is not None:
        self._ping_job.stop()
    self._clients.clear()