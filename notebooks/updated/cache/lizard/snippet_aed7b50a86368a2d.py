def request_update(self):
    with self._lock:
        self._need_update = True
        if not self._future or self._future.is_done:
            self._future = Future()
        return self._future