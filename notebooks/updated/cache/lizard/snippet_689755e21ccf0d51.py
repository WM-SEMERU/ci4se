def _close(self):
    if not self._closed:
        try:
            self._con.close()
        except Exception:
            pass
        self._transaction = False
        self._closed = True