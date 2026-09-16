async def fetchrow(self, *args, timeout=None):
    data = await self.__bind_execute(args, 1, timeout)
    if not data:
        return None
    return data[0]