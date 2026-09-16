def _has_file_rolled(self):
    if self._fh:
        size = self._getsize_of_current_file()
        if size < self.oldsize:
            return True
        self.oldsize = size
    return False