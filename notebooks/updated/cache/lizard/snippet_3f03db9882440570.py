def get_instance(self, payload):
    return CredentialInstance(self._version, payload, account_sid=self.
        _solution['account_sid'], credential_list_sid=self._solution[
        'credential_list_sid'])