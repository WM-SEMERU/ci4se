def clone(self, **override_vars):
    c = Context(self.vars, self.data)
    c.executed_actions = set(self.executed_actions)
    c.vars.update(override_vars)
    return c