def exceptlist(self, channel):
    with self.lock:
        self.is_in_channel(channel)
        self.send('MODE %s e' % channel)
        excepts = []
        while self.readable():
            msg = self._recv(expected_replies=('348', '349'))
            if msg[0] == '348':
                exceptmask, who, timestamp = msg[2].split()[1:]
                excepts.append((self._from_(exceptmask), who, self._m_time.
                    localtime(int(timestamp))))
            elif msg[0] == '349':
                break
        return excepts