def full_name(self):
    if self._full_name is None:
        self._full_name = 'projects/{project}/taskqueues/{taskqueue}'.format(
            project=self.project, taskqueue=self.id)
    return self._full_name