def get_objective_hierarchy_session_for_objective_bank(self,
    objective_bank_id, proxy):
    if not self.supports_objective_hierarchy():
        raise errors.Unimplemented()
    return sessions.ObjectiveHierarchySession(objective_bank_id, proxy,
        self._runtime)