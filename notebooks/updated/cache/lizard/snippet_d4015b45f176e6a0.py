def get_instance(self, payload):
    return DefaultsInstance(self._version, payload, assistant_sid=self.
        _solution['assistant_sid'])