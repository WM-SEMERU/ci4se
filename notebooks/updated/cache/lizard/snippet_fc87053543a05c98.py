def acquire(self):
    if self.timeout is not None:
        sleep_intervals = int(self.timeout / self.sleep_time)
    else:
        sleep_intervals = float('inf')
    while not self.acquire_try_once() and sleep_intervals > 0:
        time.sleep(self.sleep_time)
        sleep_intervals -= 1
    if not self.is_locked_by_me():
        raise util.io.filelock.general.FileLockTimeoutError(self.
            lock_filename, self.timeout)