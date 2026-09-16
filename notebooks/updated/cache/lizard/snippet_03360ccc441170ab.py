def remove_lock(self):
    key = '%s_lock' % self.scheduler_key
    if self._lock_acquired:
        self.connection.delete(key)