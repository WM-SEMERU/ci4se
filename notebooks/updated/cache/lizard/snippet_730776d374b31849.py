async def kick(self, channel, target, reason=None):
    if not self.in_channel(channel):
        raise NotInChannel(channel)
    if reason:
        await self.rawmsg('KICK', channel, target, reason)
    else:
        await self.rawmsg('KICK', channel, target)