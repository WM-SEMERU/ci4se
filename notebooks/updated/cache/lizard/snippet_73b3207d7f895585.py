def get_instance(self, payload):
    return EngagementContextInstance(self._version, payload, flow_sid=self.
        _solution['flow_sid'], engagement_sid=self._solution['engagement_sid'])