def get_bank_query_session(self):
    if not self.supports_bank_query():
        raise errors.Unimplemented()
    return sessions.BankQuerySession(runtime=self._runtime)