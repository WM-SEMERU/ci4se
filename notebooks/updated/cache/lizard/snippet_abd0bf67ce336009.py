def start(self, interval, now=True):
    if interval < 0:
        raise ValueError('interval must be >= 0')
    if self._running:
        self.stop()
    self._running = True
    self._interval = interval
    if now:
        self._self_thread = hub.spawn_after(0, self)
    else:
        self._self_thread = hub.spawn_after(self._interval, self)