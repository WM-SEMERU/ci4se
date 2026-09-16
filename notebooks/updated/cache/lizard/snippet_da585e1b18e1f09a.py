def cumulative_statistics(self):
    if self._cumulative_statistics is None:
        self._cumulative_statistics = WorkspaceCumulativeStatisticsList(self
            ._version, workspace_sid=self._solution['sid'])
    return self._cumulative_statistics