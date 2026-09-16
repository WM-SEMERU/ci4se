async def _execute(self, fn, *args, **kwargs):
    return await self._conn._execute(fn, *args, **kwargs)