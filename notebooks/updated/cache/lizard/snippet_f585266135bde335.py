def update(self, sample_sid=values.unset, status=values.unset):
    data = values.of({'SampleSid': sample_sid, 'Status': status})
    payload = self._version.update('POST', self._uri, data=data)
    return QueryInstance(self._version, payload, assistant_sid=self.
        _solution['assistant_sid'], sid=self._solution['sid'])