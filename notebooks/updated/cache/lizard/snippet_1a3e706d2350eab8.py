async def info(self, ctx, *, member: discord.Member=None):
    channel = ctx.message.channel
    if member is None:
        member = ctx.message.author
    e = discord.Embed()
    roles = [role.name.replace('@', '@\u200b') for role in member.roles]
    shared = sum(1 for m in self.bot.get_all_members() if m.id == member.id)
    voice = member.voice_channel
    if voice is not None:
        other_people = len(voice.voice_members) - 1
        voice_fmt = '{} with {} others' if other_people else '{} by themselves'
        voice = voice_fmt.format(voice.name, other_people)
    else:
        voice = 'Not connected.'
    e.set_author(name=str(member), icon_url=member.avatar_url or member.
        default_avatar_url)
    e.set_footer(text='Member since').timestamp = member.joined_at
    e.add_field(name='ID', value=member.id)
    e.add_field(name='Servers', value='%s shared' % shared)
    e.add_field(name='Voice', value=voice)
    e.add_field(name='Created', value=member.created_at)
    e.add_field(name='Roles', value=', '.join(roles))
    e.colour = member.colour
    if member.avatar:
        e.set_image(url=member.avatar_url)
    await self.bot.say(embed=e)