def request_check_all(self, wait_time=5):
    with self._lock:
        self._request_check_all()
        self._condition.wait(wait_time)