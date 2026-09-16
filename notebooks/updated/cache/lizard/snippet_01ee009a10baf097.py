def invitelist(self, channel):
    with self.lock:
        self.is_in_channel(channel)
        self.send('MODE %s i' % channel)
        invites = []
        while self.readable():
            msg = self._recv(expected_replies=('346', '347'))
            if msg[0] == '346':
                invitemask, who, timestamp = msg[2].split()[1:]
                invites.append((self._from_(invitemask), who, self._m_time.
                    localtime(int(timestamp))))
            elif msg[0] == '347':
                break
        return invites