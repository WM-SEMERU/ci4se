def shutdown(self):
    if not self._stop_evt:
        return
    self.reactor.removeSystemEventTrigger(self._stop_evt)
    self._stop()