def add_policy_statements(self, statements):
    if isinstance(statements, Statement):
        statements = [statements]
    self._policy_statements.extend(statements)