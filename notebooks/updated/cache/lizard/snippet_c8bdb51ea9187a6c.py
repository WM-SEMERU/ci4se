def closed(self, code, reason=None):
    if code != 1000:
        self._error = errors.SignalFlowException(code, reason)
        _logger.info('Lost WebSocket connection with %s (%s: %s).', self,
            code, reason)
        for c in self._channels.values():
            c.offer(WebSocketComputationChannel.END_SENTINEL)
    self._channels.clear()
    with self._connection_cv:
        self._connected = False
        self._connection_cv.notify()