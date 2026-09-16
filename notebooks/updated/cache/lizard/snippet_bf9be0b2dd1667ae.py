def min(self, expr, extra_constraints=(), solver=None, model_callback=None):
    if self._solver_required and solver is None:
        raise BackendError('%s requires a solver for evaluation' % self.
            __class__.__name__)
    return self._min(self.convert(expr), extra_constraints=self.
        convert_list(extra_constraints), solver=solver, model_callback=
        model_callback)