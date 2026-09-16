async def _ask_queue_update(self):
    try:
        while True:
            await asyncio.sleep(self._queue_update_timer)
            if (self._queue_update_last_attempt == 0 or self.
                _queue_update_last_attempt > self.
                _queue_update_last_attempt_max):
                if self._queue_update_last_attempt:
                    self._logger.error(
                        'Asking for a job queue update despite previous update not yet received'
                        )
                else:
                    self._logger.debug('Asking for a job queue update')
                self._queue_update_last_attempt = 1
                await self._simple_send(ClientGetQueue())
            else:
                self._logger.error(
                    'Not asking for a job queue update as previous update not yet received'
                    )
    except asyncio.CancelledError:
        return
    except KeyboardInterrupt:
        return