def stop(self):
    if self._start_instant is None:
        raise IntervalException(
            'Attempt to stop an interval that has not started.')
    if self._stop_instant is None:
        self._stop_instant = instant()
        self._duration = int((self._stop_instant - self._start_instant) * 1000)
        return self._duration
    return False