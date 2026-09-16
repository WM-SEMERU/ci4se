def get(self, sid):
    return TaskChannelContext(self._version, workspace_sid=self._solution[
        'workspace_sid'], sid=sid)