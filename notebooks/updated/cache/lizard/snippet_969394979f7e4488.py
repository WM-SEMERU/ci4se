async def executemany(self, command: str, args, *, timeout: float=None):
    self._check_open()
    return await self._executemany(command, args, timeout)