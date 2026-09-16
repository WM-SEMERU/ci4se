def fetch(self):
    params = values.of({})
    payload = self._version.fetch('GET', self._uri, params=params)
    return AssignedAddOnInstance(self._version, payload, account_sid=self.
        _solution['account_sid'], resource_sid=self._solution[
        'resource_sid'], sid=self._solution['sid'])