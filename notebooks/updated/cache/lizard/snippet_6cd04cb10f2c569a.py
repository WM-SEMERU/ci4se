def end(self):
    if self.keeper.enabled:
        if self._begin_time is None:
            raise RuntimeError('end() called without preceding begin()')
        dt = time.time() - self._begin_time
        self._begin_time = None
        self._count += 1
        self._sum += dt
        if dt > self._max:
            self._max = dt
        if dt < self._min:
            self._min = dt