def get_instance(self, payload):
    return CredentialListMappingInstance(self._version, payload,
        account_sid=self._solution['account_sid'], domain_sid=self.
        _solution['domain_sid'])