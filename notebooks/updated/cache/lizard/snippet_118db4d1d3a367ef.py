async def kickban(self, channel, target, reason=None, range=0):
    await self.ban(channel, target, range)
    await self.kick(channel, target, reason)