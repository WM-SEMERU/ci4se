def satisfiable(self, **kwargs):
    if o.ABSTRACT_SOLVER in self.options or o.SYMBOLIC not in self.options:
        extra_constraints = kwargs.pop('extra_constraints', ())
        for e in extra_constraints:
            if self.solver.is_false(e):
                return False
        return self._satisfiable
    else:
        return self.solver.satisfiable(**kwargs)