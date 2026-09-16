def clear_lock(self, key):
    lock_path = self._get_lock_path(key)
    os.remove(lock_path)