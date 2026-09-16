def timing(self, stat, delta, rate=1):
    if isinstance(delta, timedelta):
        delta = delta.total_seconds() * 1000.0
    self._send_stat(stat, '%0.6f|ms' % delta, rate)