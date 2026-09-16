def cancel(self):
    with self._lock:
        if self._state not in (self.S_PENDING, self.S_RUNNING):
            return False
        self._result = Cancelled('cancelled by Future.cancel()')
        self._state = self.S_EXCEPTION
        self._done.set()
        return True