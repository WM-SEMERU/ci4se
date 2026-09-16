def solve(self, reaction_1, reaction_2):
    self._prob.set_objective(self._vbow(reaction_1))
    if self._reaction_constr is not None:
        self._reaction_constr.delete()
    self._reaction_constr, = self._prob.add_linear_constraints(self._vbow(
        reaction_2) == 1)
    results = []
    for sense in (lp.ObjectiveSense.Minimize, lp.ObjectiveSense.Maximize):
        try:
            result = self._prob.solve(sense)
        except lp.SolverError:
            results.append(None)
        else:
            results.append(result.get_value(self._vbow(reaction_1)))
    return tuple(results)