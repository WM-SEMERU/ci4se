def run(self):
    with self._run_lock:
        while self.mounts:
            for mount in self.mounts:
                try:
                    next(mount)
                except StopIteration:
                    self.mounts.remove(mount)