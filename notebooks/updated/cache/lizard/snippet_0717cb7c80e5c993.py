def add_constraint(self, name, coefficients={}, ub=0):
    if name in self._constraints:
        raise ValueError('A constraint named ' + name + ' already exists.')
    self._constraints[name] = len(self._constraints)
    self.upper_bounds = np.append(self.upper_bounds, ub)
    new_row = np.array([[coefficients.get(name, 0) for name in self.
        _variables]])
    self._add_row_to_A(new_row)
    self._reset_solution()