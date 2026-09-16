def _read_channel(self):
    if self.protocol == 'ssh':
        output = ''
        while True:
            if self.remote_conn.recv_ready():
                outbuf = self.remote_conn.recv(MAX_BUFFER)
                if len(outbuf) == 0:
                    raise EOFError('Channel stream closed by remote device.')
                output += outbuf.decode('utf-8', 'ignore')
            else:
                break
    elif self.protocol == 'telnet':
        output = self.remote_conn.read_very_eager().decode('utf-8', 'ignore')
    elif self.protocol == 'serial':
        output = ''
        while self.remote_conn.in_waiting > 0:
            output += self.remote_conn.read(self.remote_conn.in_waiting
                ).decode('utf-8', 'ignore')
    log.debug('read_channel: {}'.format(output))
    self._write_session_log(output)
    return output