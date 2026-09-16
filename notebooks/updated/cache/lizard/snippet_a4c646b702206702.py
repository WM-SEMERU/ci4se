def is_nsfw():

    def pred(ctx):
        ch = ctx.channel
        if ctx.guild is None or isinstance(ch, discord.TextChannel
            ) and ch.is_nsfw():
            return True
        raise NSFWChannelRequired(ch)
    return check(pred)