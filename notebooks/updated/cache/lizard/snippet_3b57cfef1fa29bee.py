def get_instance(self, payload):
    return TaskInstance(self._version, payload, workspace_sid=self.
        _solution['workspace_sid'])