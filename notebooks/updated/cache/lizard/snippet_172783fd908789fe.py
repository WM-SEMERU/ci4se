async def _all(self, ctx):
    ignored = self.config.get('ignored', [])
    channels = ctx.message.server.channels
    ignored.extend(c.id for c in channels if c.type == discord.ChannelType.text
        )
    await self.config.put('ignored', list(set(ignored)))
    await self.bot.responses.success(message='All channels ignored.')