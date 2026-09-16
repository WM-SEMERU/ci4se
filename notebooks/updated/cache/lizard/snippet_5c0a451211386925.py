def send(self, datum):
    try:
        self._p.stdin.write(datum.rstrip() + '\n')
        self._p.stdin.flush()
    except (IOError, OSError):
        logging.info(
            'Attempted to write to a closed process; attempting to reopen')
        self._open()
        self._p.stdin.write(datum.rstrip() + '\n')
        self._p.stdin.flush()