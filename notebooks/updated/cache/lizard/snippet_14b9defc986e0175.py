async def volume(self, ctx, volume: int):
    if ctx.voice_client is None:
        return await ctx.send('Not connected to a voice channel.')
    ctx.voice_client.source.volume = volume / 100
    await ctx.send('Changed volume to {}%'.format(volume))