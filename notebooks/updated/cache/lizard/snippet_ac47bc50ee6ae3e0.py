def start(self, initial_delay=0):
    if self.listener is None:
        raise exceptions.NoAsyncListenerError
    elif self._enabled:
        return
    self._enabled = True