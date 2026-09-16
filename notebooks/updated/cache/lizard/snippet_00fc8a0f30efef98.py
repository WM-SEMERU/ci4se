def directory(self):
    if not self.is_directory:
        msg = 'This task is a file task with no associated directory.'
        raise TaskError(msg)
    if self._directory is None:
        if self.is_transferred:
            self._directory = self.api._load_directory(self.cid)
    if self._directory is None:
        msg = ('No directory assciated with this task: Task is %s.' % self.
            status_human.lower())
        raise TaskError(msg)
    return self._directory