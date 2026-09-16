def remove_constraint(self, name):
    index = self._get_constraint_index(name)
    self._A = np.delete(self.A, index, 0)
    self.upper_bounds = np.delete(self.upper_bounds, index)
    del self._constraints[name]
    self._update_constraint_indices()
    self._reset_solution()