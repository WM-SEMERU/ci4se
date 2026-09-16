def get_instance(self, payload):
    return PhoneNumberInstance(self._version, payload, trunk_sid=self.
        _solution['trunk_sid'])