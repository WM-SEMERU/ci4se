def get_log_hierarchy_design_session(self, proxy):
    if not self.supports_log_hierarchy_design():
        raise errors.Unimplemented()
    return sessions.LogHierarchyDesignSession(proxy=proxy, runtime=self.
        _runtime)