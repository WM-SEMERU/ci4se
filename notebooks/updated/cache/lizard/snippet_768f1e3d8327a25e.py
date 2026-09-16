def create(self, to, channel, custom_message=values.unset):
    data = values.of({'To': to, 'Channel': channel, 'CustomMessage':
        custom_message})
    payload = self._version.create('POST', self._uri, data=data)
    return VerificationInstance(self._version, payload, service_sid=self.
        _solution['service_sid'])