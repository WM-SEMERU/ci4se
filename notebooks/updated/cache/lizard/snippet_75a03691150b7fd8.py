def get_objective_lookup_session_for_objective_bank(self, objective_bank_id,
    proxy):
    if not self.supports_objective_lookup():
        raise errors.Unimplemented()
    return sessions.ObjectiveLookupSession(objective_bank_id, proxy, self.
        _runtime)