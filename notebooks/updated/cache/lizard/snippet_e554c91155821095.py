def clear(self):
    for walker in self._virtual_walkers:
        walker.skip_all()
    self._engine.clear()
    for walker in self._queue_walkers:
        walker.skip_all()
    self._last_values = {}