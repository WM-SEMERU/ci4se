def create(self, name, code_length=values.unset):
    data = values.of({'Name': name, 'CodeLength': code_length})
    payload = self._version.create('POST', self._uri, data=data)
    return ServiceInstance(self._version, payload)