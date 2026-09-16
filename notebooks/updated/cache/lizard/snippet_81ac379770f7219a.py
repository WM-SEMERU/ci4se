def signal(self, details):
    log = self._params.get('log', self._discard)
    if '_signal' not in dir(self._parent) or not callable(getattr(self.
        _parent, '_signal')):
        log.error("Event parent '%s' has no '_signal' method", self._name)
        return
    sig = utils.signum(self._handler_arg)
    if sig is None:
        log.error("Invalid signal '%s' for task '%s'", self._handler_arg,
            sig._name)
        return
    log.info("sending %s to all '%s' processes", utils.signame(sig), self._name
        )
    self._parent._signal(sig)