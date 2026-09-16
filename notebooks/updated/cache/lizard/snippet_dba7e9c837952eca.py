def statistics(self):
    if self._statistics is None:
        self._statistics = WorkflowStatisticsList(self._version,
            workspace_sid=self._solution['workspace_sid'], workflow_sid=
            self._solution['sid'])
    return self._statistics