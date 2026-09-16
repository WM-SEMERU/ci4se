def create(self, type, friendly_name=values.unset, certificate=values.unset,
    private_key=values.unset, sandbox=values.unset, api_key=values.unset,
    secret=values.unset):
    data = values.of({'Type': type, 'FriendlyName': friendly_name,
        'Certificate': certificate, 'PrivateKey': private_key, 'Sandbox':
        sandbox, 'ApiKey': api_key, 'Secret': secret})
    payload = self._version.create('POST', self._uri, data=data)
    return CredentialInstance(self._version, payload)