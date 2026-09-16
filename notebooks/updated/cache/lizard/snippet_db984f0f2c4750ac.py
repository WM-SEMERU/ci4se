def forget(self):
    self._observed_events = {}
    if self in self._observers:
        self._observers.remove(self)