def acquire_writer(self):
    with self.mutex:
        while self.rwlock != 0:
            self._writer_wait()
        self.rwlock = -1