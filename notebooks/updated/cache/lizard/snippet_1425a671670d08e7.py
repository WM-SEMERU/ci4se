def on(self, evt, func):
    if evt not in self._callbacks:
        raise NotImplementedError('callback "%s"' % evt)
    else:
        self._callbacks[evt] = func