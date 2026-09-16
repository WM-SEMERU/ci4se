async def _stop_internal(self):
    if self.stopping is True:
        return
    self.stopping = True
    awaitables = [task.stop() for task in self.tasks]
    results = await asyncio.gather(*awaitables, return_exceptions=True)
    for task, result in zip(self.tasks, results):
        if isinstance(result, Exception):
            self._logger.error('Error stopping task %s: %s', task.name,
                repr(result))
    self.loop.call_soon(self.loop.stop)