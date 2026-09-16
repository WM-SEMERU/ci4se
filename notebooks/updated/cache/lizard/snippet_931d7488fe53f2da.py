async def close(self):
    if not self._conn:
        return
    c = await self._execute(self._conn.close)
    self._conn = None
    return c