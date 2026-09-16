async def hset(self, name, key, value):
    return await self.execute_command('HSET', name, key, value)