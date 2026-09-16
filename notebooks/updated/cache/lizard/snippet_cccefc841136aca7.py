def _timeout_expired(self):
    self._did_timeout = True
    try:
        self.transport.signalProcess('TERM')
    except error.ProcessExitedAlready:
        self.transport.loseConnection()
    fail = Failure(RuntimeError('timeout while launching Tor'))
    self._maybe_notify_connected(fail)