def stop(self, subname='total'):
    assert self._stop is None, 'Unable to stop, the timer is already stopped'
    self._stop = time.time()
    return self.send(subname, self._stop - self._start)