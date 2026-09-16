async def register(self, channel, event, callback):
    channel = self.channel(channel)
    event = channel.register(event, callback)
    await channel.connect(event.name)
    return channel