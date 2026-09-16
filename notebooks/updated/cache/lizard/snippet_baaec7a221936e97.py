async def sdiffstore(self, dest, keys, *args):
    args = list_or_args(keys, args)
    return await self.execute_command('SDIFFSTORE', dest, *args)