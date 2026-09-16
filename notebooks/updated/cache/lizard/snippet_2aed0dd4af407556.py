async def _start(self):
    self.agent._alive.wait()
    try:
        await self.on_start()
    except Exception as e:
        logger.error('Exception running on_start in behaviour {}: {}'.
            format(self, e))
        self.kill(exit_code=e)
    await self._step()
    self._is_done.clear()