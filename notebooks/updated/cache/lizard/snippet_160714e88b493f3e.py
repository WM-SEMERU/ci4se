async def fetchval(self, query, *args, column=0, timeout=None):
    async with self.acquire() as con:
        return await con.fetchval(query, *args, column=column, timeout=timeout)