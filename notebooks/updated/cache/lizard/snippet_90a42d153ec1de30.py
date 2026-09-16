def text_channels(self):
    ret = [c for c in self.guild.channels if c.category_id == self.id and
        isinstance(c, TextChannel)]
    ret.sort(key=lambda c: (c.position, c.id))
    return ret