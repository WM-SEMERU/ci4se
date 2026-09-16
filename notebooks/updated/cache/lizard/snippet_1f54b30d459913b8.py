def create(self, phone_number_sid):
    data = values.of({'PhoneNumberSid': phone_number_sid})
    payload = self._version.create('POST', self._uri, data=data)
    return PhoneNumberInstance(self._version, payload, service_sid=self.
        _solution['service_sid'])