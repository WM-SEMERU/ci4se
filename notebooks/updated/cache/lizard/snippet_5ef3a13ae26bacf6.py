def get_instance(self, payload):
    return NewSigningKeyInstance(self._version, payload, account_sid=self.
        _solution['account_sid'])