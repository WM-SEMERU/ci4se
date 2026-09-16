async def clear(self):
    with (await self._cond):
        while self._free:
            conn = self._free.popleft()
            await conn.close()
        self._cond.notify()