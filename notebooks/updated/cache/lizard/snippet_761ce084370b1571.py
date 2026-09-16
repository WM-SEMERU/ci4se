def _do_autocommit(self):
    self._commit_counter += 1
    if isinstance(self._autocommit, bool) and self._autocommit:
        self.commit()
        self._commit_counter = 0
    elif isinstance(self._autocommit, int) and self._autocommit > 0:
        if self._commit_counter % self._autocommit == 0:
            self.commit()
            self._commit_counter = 0