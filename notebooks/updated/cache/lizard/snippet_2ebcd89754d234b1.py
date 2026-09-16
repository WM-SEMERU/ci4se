def connectionLost(self, reason=connectionDone):
    self._failed = reason
    pending, self._pending = self._pending, None
    for d in pending.values():
        d.errback(reason)