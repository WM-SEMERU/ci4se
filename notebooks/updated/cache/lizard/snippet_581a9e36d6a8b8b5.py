def run(self):
    _LOGGER.info('Started')
    while True:
        self._maybe_reconnect()
        line = ''
        try:
            t = self._telnet
            if t is not None:
                line = t.read_until(b'\n')
        except EOFError:
            try:
                self._lock.acquire()
                self._disconnect_locked()
                continue
            finally:
                self._lock.release()
        self._recv_cb(line.decode('ascii').rstrip())