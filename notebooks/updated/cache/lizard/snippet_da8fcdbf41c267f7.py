def _loop(self, *args, **kwargs):
    self.on_start(*self.on_start_args, **self.on_start_kwargs)
    try:
        while not self._stop_signal:
            self.target(*args, **kwargs)
    finally:
        self.on_stop(*self.on_stop_args, **self.on_stop_kwargs)
        self._stop_signal = False
        self._lock.set()