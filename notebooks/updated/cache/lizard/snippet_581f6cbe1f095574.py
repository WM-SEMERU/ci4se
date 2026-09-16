def _run(self):
    tup = self.read_tuple()
    with self._batch_lock:
        self._current_tups = [tup]
        if self.is_heartbeat(tup):
            self.send_message({'command': 'sync'})
        elif self.is_tick(tup):
            self.process_tick(tup)
        else:
            self.process(tup)
        self._current_tups = []