def get_bank_lookup_session(self):
    if not self.supports_bank_lookup():
        raise errors.Unimplemented()
    return sessions.BankLookupSession(runtime=self._runtime)