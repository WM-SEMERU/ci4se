async def is_locked(self, resource):
    with (await self.connect()) as redis:
        lock_identifier = await redis.get(resource)
    if lock_identifier:
        return True
    else:
        return False