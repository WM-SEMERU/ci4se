def add_done_callback(self, fun):
    with self._lock:
        if self._completed:
            fun()
        else:
            self._done_callbacks.append(fun)