def _ncomponents(self):
    return [sympy_to_py(expr, self.independent_vars + self.dependent_vars +
        self.params) for expr in self.values()]