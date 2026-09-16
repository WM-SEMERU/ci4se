def get_instance(self, payload):
    return WebhookInstance(self._version, payload, session_sid=self.
        _solution['session_sid'])