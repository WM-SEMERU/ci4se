def go(self):
    DEBUG and self._name and Log.note('GO! {{name|quote}}', name=self.name)
    if self._go:
        return
    with self.lock:
        if self._go:
            return
        self._go = True
    DEBUG and self._name and Log.note('internal GO! {{name|quote}}', name=
        self.name)
    jobs, self.job_queue = self.job_queue, None
    threads, self.waiting_threads = self.waiting_threads, None
    if threads:
        DEBUG and self._name and Log.note('Release {{num}} threads', num=
            len(threads))
        for t in threads:
            t.release()
    if jobs:
        for j in jobs:
            try:
                j()
            except Exception as e:
                Log.warning('Trigger on Signal.go() failed!', cause=e)