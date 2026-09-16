def fetch(self):
    params = values.of({})
    payload = self._version.fetch('GET', self._uri, params=params)
    return InviteInstance(self._version, payload, service_sid=self.
        _solution['service_sid'], channel_sid=self._solution['channel_sid'],
        sid=self._solution['sid'])