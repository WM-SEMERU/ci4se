def squit(self, server, reason=''):
    with self.lock:
        self.send('SQUIT %s :%s' % (server, reason))
        while self.readable():
            msg = self._recv(expected_replies=('SQUIT',))
            if msg[0] == 'SQUIT':
                if not self.hide_called_events:
                    self.stepback()