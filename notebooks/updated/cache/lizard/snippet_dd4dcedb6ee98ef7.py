def wait(self, timeout=None):
    self._event.wait(timeout)
    return self._event.isSet()