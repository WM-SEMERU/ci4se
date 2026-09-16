def get_instance(self, payload):
    return UserInstance(self._version, payload, service_sid=self._solution[
        'service_sid'])