async def emit(self, record: LogRecord):
    try:
        if self.should_rollover(record):
            async with self._rollover_lock:
                if self.should_rollover(record):
                    await self.do_rollover()
        await super().emit(record)
    except Exception as e:
        await self.handleError(record)