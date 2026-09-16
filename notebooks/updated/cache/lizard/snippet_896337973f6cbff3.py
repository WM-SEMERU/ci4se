def fetch(self):
    params = values.of({})
    payload = self._version.fetch('GET', self._uri, params=params)
    return MemberInstance(self._version, payload, account_sid=self.
        _solution['account_sid'], queue_sid=self._solution['queue_sid'],
        call_sid=self._solution['call_sid'])