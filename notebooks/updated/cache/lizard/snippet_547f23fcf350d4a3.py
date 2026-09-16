def update(self, body=values.unset, attributes=values.unset):
    data = values.of({'Body': body, 'Attributes': attributes})
    payload = self._version.update('POST', self._uri, data=data)
    return MessageInstance(self._version, payload, service_sid=self.
        _solution['service_sid'], channel_sid=self._solution['channel_sid'],
        sid=self._solution['sid'])