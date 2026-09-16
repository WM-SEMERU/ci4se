def assertSignalNotFired(self, signal, *args, **kwargs):
    event = signal, args, kwargs
    self.assertNotIn(event, self._events_seen,
        '\nSignal unexpectedly fired: {}\n'.format(event))