def connect(self, event, func=None):
    if event not in self._callbacks:
        raise ValueError('{!r} is not a valid cursor event'.format(event))
    if func is None:
        return partial(self.connect, event)
    self._callbacks[event].append(func)
    return func