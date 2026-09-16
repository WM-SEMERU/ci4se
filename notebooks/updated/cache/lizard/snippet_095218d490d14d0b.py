def add_constraint(self, func, variables, default_values=None):
    self._constraints.append((func, variables, default_values or ()))