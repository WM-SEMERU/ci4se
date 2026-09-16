def send(self):
    buf_sz = 500
    to_send = {}
    for mn in self.data.iterkeys():
        while len(self.data[mn]) > 0:
            l = len(to_send)
            if l < buf_sz:
                to_send.setdefault(mn, [])
                to_send[mn].append(self.data[mn].pop())
            else:
                try:
                    self._send(to_send)
                    to_send = {}
                    to_send.setdefault(mn, [])
                    to_send[mn].append(self.data[mn].pop())
                except socket.error:
                    self.logger.error(
                        'Error sending to carbon, trying to reconnect.')
                    self.sock = self._connect()
                    for ent in to_send:
                        self.data[ent[0]].append(ent[1])
    try:
        self._send(to_send)
    except socket.error:
        self.logger.error('Error sending to carbon, trying to reconnect.')
        self.sock = self._connect()
    for ent in to_send:
        self.data[ent[0]].append(ent[1])