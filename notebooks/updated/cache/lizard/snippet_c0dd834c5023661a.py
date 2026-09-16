def _is_modified(self, filepath):
    if self._is_new(filepath):
        return False
    mtime = self._get_modified_time(filepath)
    return self._watched_files[filepath] < mtime