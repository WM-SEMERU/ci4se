def kick(self, channel, nick, reason=''):
    with self.lock:
        self.is_in_channel(channel)
        self.send('KICK %s %s :%s' % (channel, nick, reason))
        if self.readable():
            msg = self._recv(expected_replies=('KICK',))
            if msg[0] == 'KICK':
                channel = msg[1]
                if not self.hide_called_events:
                    self.stepback()
        if self.compare(self.current_nick, nick):
            del self.channels[channel]