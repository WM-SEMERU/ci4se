def close(self):
    super(LockingDatabase, self).close()
    if not self.readonly:
        self.release_lock()