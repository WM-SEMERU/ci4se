async def cancel(self):
    self.is_cancelled = True
    if self.future is not None:
        self.future.cancel()
    if self.task_process is not None:
        log.warning(
            'Worker is shutting down, but a task is running. Terminating task')
        await self.task_process.worker_shutdown_stop()