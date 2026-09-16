def get_objective_hierarchy_design_session_for_objective_bank(self,
    objective_bank_id, proxy):
    if not self.supports_objective_hierarchy_design():
        raise errors.Unimplemented()
    return sessions.ObjectiveHierarchyDesignSession(objective_bank_id,
        proxy, self._runtime)