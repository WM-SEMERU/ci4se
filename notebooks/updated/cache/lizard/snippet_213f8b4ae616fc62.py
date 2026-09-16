def _force_close(self):
    if self._sock:
        try:
            self._sock.close()
        except:
            pass
    self._sock = None
    self._rfile = None