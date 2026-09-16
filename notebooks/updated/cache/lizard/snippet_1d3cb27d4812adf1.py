def create(self, key, value):
    data = values.of({'Key': key, 'Value': value})
    payload = self._version.create('POST', self._uri, data=data)
    return VariableInstance(self._version, payload, service_sid=self.
        _solution['service_sid'], environment_sid=self._solution[
        'environment_sid'])