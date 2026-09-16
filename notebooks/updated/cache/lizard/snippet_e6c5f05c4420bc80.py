def rset(self):
    self._send('RSET\r\n')
    resp = self._read()
    if not resp.startswith('250'):
        logger.warn('Unexpected server response at RSET: ' + resp)
    self._recipients = []
    self.results = {}