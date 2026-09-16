def _finish(self):
    if self.active and self.cnt >= self.max_iter:
        self.total_time = self._elapsed()
        self.end = time.time()
        self.last_progress -= 1
        self._print()
        if self.track:
            self._stream_out('\nTotal time elapsed: ' + self._get_time(self
                .total_time))
        self._stream_out('\n')
        self.active = False