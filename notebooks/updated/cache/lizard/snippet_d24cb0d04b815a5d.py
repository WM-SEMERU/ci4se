def reconstrain(self):
    subsolvers = self.state.solver._solver.split()
    for solver in subsolvers:
        solver.timeout = 1000 * 10
        if not solver.satisfiable():
            for var in solver.variables:
                if var in self.variable_map:
                    self.state.solver.add(self.variable_map[var])
                else:
                    l.warning('var %s not found in self.variable_map', var)