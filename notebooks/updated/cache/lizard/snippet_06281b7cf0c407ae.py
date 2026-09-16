def unmount(self, path):
    del self._mountpoints[self._join_chunks(self._normalize_path(path))]