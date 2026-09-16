def fileno(self):
    self.lock.acquire()
    try:
        if self._pipe is not None:
            return self._pipe.fileno()
        self._pipe = pipe.make_pipe()
        p1, p2 = pipe.make_or_pipe(self._pipe)
        self.in_buffer.set_event(p1)
        self.in_stderr_buffer.set_event(p2)
        return self._pipe.fileno()
    finally:
        self.lock.release()