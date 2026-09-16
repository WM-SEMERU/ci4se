async def cursor_async(self):
    await self.connect_async(loop=self._loop)
    if self.transaction_depth_async() > 0:
        conn = self.transaction_conn_async()
    else:
        conn = None
    try:
        return await self._async_conn.cursor(conn=conn)
    except:
        await self.close_async()
        raise