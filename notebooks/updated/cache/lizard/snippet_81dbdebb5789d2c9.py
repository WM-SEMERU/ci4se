def on_invite(self, connection, event):
    sender = self.get_nick(event.source)
    invited = self.get_nick(event.target)
    channel = event.arguments[0]
    if invited == self._nickname:
        logging.info('! I am invited to %s by %s', channel, sender)
        connection.join(channel)
    else:
        logging.info('>> %s invited %s to %s', sender, invited, channel)