def _read_protocol_line(self):
    while True:
        line = self._proc.stdout.readline().decode('utf-8')
        if not line:
            raise jsonrpc_client_base.AppStartError(self._ad,
                'Unexpected EOF waiting for app to start')
        line = line.strip()
        if line.startswith('INSTRUMENTATION_RESULT:') or line.startswith(
            'SNIPPET '):
            self.log.debug('Accepted line from instrumentation output: "%s"',
                line)
            return line
        self.log.debug('Discarded line from instrumentation output: "%s"', line
            )