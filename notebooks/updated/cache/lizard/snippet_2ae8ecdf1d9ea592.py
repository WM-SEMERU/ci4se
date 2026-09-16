def set_timeout(self, timeout=None, code=None):
    if timeout is None:
        timeout = self.args.timeout if self.args.timeout else 10
    if code is None:
        code = UNKNOWN
    self._timeout_delay = timeout
    self._timeout_code = code
    signal.signal(signal.SIGALRM, self._timeout_handler)
    signal.alarm(timeout)