def has_false(self, e, extra_constraints=(), solver=None, model_callback=None):
    return self._has_false(self.convert(e), extra_constraints=
        extra_constraints, solver=solver, model_callback=model_callback)