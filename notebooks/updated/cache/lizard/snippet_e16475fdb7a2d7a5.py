def engagements(self):
    if self._engagements is None:
        self._engagements = EngagementList(self._version, flow_sid=self.
            _solution['sid'])
    return self._engagements