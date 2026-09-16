def activate(self):
    if 'activate' in self.data.links:
        self.make_request(ActionCommandFailed, method='update', etag=self.
            etag, resource='activate')
        self._del_cache()
    else:
        raise ActionCommandFailed(
            'Task is already activated. To suspend, call suspend() on this task schedule'
            )