def unbounded(self):
    self._check_valid()
    status = self._problem._p.Status
    if (status == gurobipy.GRB.INF_OR_UNBD and self._problem._p.params.
        DualReductions):
        self._problem._p.params.DualReductions = 0
        try:
            self._problem._p.optimize()
        finally:
            self._problem._p.params.DualReductions = 1
        status = self._problem._p.Status
    return status == gurobipy.GRB.UNBOUNDED