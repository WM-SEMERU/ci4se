def halt(self):
    if self._callback:
        self._thread_continue = False
        self._thread.join()