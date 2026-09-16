def _assemble(self):
    for stmt in self.statements:
        pol = self.processed_policies[stmt.uuid]
        if _is_whitelisted(stmt):
            self._dispatch(stmt, 'assemble', self.model, self.agent_set,
                pol.parameters)