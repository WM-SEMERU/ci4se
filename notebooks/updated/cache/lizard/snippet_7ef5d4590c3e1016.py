def run(self):
    while True:
        with self._lock:
            self._update(self._data)
        if self._done:
            break
        time.sleep(1)