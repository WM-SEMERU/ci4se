def _send(self, data):
    retry = self.RETRY
    while retry > 0:
        if not self.socket:
            self.log.error('StatsiteHandler: Socket unavailable.')
            self._connect()
            retry -= 1
            continue
        try:
            data = data.split()
            data = data[0] + ':' + data[1] + '|kv\n'
            self.socket.sendall(data)
            break
        except socket.error as e:
            self.log.error('StatsiteHandler: Failed sending data. %s.', e)
            self._close()
            retry -= 1
            continue