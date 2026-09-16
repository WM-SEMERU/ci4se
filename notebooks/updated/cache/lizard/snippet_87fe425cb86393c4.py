def notify_all(self):
    if not self._is_owned():
        raise RuntimeError('cannot wait on un-acquired lock')
    scheduler.state.awoken_from_events.update(x[0] for x in self._waiters)
    self._waiters.clear()