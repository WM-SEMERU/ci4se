async def connect(self):
    assert not self.closed
    connection = await self._get()
    return PoolConnection(self, connection)