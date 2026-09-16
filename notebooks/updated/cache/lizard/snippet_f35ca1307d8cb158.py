def create(self, identity, binding_type, address, tag=values.unset,
    notification_protocol_version=values.unset, credential_sid=values.unset,
    endpoint=values.unset):
    data = values.of({'Identity': identity, 'BindingType': binding_type,
        'Address': address, 'Tag': serialize.map(tag, lambda e: e),
        'NotificationProtocolVersion': notification_protocol_version,
        'CredentialSid': credential_sid, 'Endpoint': endpoint})
    payload = self._version.create('POST', self._uri, data=data)
    return BindingInstance(self._version, payload, service_sid=self.
        _solution['service_sid'])