def solve_unchecked(self, sense=None):
    if sense is not None:
        self.set_objective_sense(sense)
    self._p.solve()
    self._result = Result(self)
    return self._result