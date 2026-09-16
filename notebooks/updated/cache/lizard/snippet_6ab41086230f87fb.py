def get_objective_hierarchy_design_session(self, proxy):
    if not self.supports_objective_hierarchy_design():
        raise errors.Unimplemented()
    return sessions.ObjectiveHierarchyDesignSession(proxy=proxy, runtime=
        self._runtime)