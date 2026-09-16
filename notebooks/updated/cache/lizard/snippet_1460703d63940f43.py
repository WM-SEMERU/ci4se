async def close_async(self):
    if self._async_wait:
        await self._async_wait
    if self._async_conn:
        conn = self._async_conn
        self._async_conn = None
        self._async_wait = None
        self._task_data = None
        await conn.close()