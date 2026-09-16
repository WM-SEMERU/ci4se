async def connect_async(self, loop=None, timeout=None):
    if self.deferred:
        raise Exception(
            'Error, database not properly initialized before opening connection'
            )
    if self._async_conn:
        return
    elif self._async_wait:
        await self._async_wait
    else:
        self._loop = loop
        self._async_wait = asyncio.Future(loop=self._loop)
        conn = self._async_conn_cls(database=self.database, loop=self._loop,
            timeout=timeout, **self.connect_params_async)
        try:
            await conn.connect()
        except Exception as e:
            if not self._async_wait.done():
                self._async_wait.set_exception(e)
            self._async_wait = None
            raise
        else:
            self._task_data = TaskLocals(loop=self._loop)
            self._async_conn = conn
            self._async_wait.set_result(True)