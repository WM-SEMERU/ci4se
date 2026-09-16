async def stop(self, _task=None):
    self._logger.info('Stopping adapter wrapper')
    if self._task.stopped:
        return
    for task in self._task.subtasks:
        await task.stop()
    self._logger.debug('Stopping underlying adapter %s', self._adapter.
        __class__.__name__)
    await self._execute(self._adapter.stop_sync)