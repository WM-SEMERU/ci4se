def statistics(self):
    if self._statistics is None:
        self._statistics = WorkspaceStatisticsList(self._version,
            workspace_sid=self._solution['sid'])
    return self._statistics