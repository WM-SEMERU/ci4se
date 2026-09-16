def part(self, channel):
    if channel in self.channels:
        channel.users.remove(self.nick)
        self.channels.remove(channel)