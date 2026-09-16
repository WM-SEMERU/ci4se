def update(self, job_binary_id, data):
    if self.version >= 2:
        UPDATE_FUNC = self._patch
    else:
        UPDATE_FUNC = self._update
    return UPDATE_FUNC('/job-binaries/%s' % job_binary_id, data, 'job_binary')