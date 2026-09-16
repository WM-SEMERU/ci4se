def shutdown(self):
    self._shuttingDown = {key: Deferred() for key in self.cachedConnections
        .keys()}
    return DeferredList([maybeDeferred(p.transport.loseConnection) for p in
        self.cachedConnections.values()] + self._shuttingDown.values())