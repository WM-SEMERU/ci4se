def _register_idle(self, idle_time, callback):
    self._idle_callback = callback
    self._idle_time = idle_time