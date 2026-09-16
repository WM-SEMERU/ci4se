def _send(self):
    try:
        try:
            if self.socket is None:
                self.log.debug(
                    'GraphiteHandler: Socket is not connected. Reconnecting.')
                self._connect()
            if self.socket is None:
                self.log.debug('GraphiteHandler: Reconnect failed.')
            else:
                self._send_data(''.join(self.metrics))
                self.metrics = []
                if self._time_to_reconnect():
                    self._close()
        except Exception:
            self._close()
            self._throttle_error('GraphiteHandler: Error sending metrics.')
            raise
    finally:
        if len(self.metrics) >= self.batch_size * self.max_backlog_multiplier:
            trim_offset = self.batch_size * self.trim_backlog_multiplier * -1
            self.log.warn('GraphiteHandler: Trimming backlog. Removing' +
                ' oldest %d and keeping newest %d metrics', len(self.
                metrics) - abs(trim_offset), abs(trim_offset))
            self.metrics = self.metrics[trim_offset:]