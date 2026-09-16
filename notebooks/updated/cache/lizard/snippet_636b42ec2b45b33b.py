def _read_incoming(self):
    fileno = self.proc.stdout.fileno()
    while 1:
        buf = b''
        try:
            buf = os.read(fileno, 1024)
        except OSError as e:
            self._log(e, 'read')
        if not buf:
            self._read_queue.put(None)
            return
        self._read_queue.put(buf)