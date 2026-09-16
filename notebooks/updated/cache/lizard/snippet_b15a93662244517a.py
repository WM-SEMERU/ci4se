def get_proficiency_lookup_session_for_objective_bank(self,
    objective_bank_id, proxy):
    if not self.supports_proficiency_lookup():
        raise errors.Unimplemented()
    return sessions.ProficiencyLookupSession(objective_bank_id, proxy, self
        ._runtime)