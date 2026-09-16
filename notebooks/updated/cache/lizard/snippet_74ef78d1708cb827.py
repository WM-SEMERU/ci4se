def _call_in_reactor_thread(self, f, *args, **kwargs):
    self._reactor.callFromThread(f, *args, **kwargs)