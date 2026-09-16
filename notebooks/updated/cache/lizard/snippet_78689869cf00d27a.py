def create_from_eflux(cls, params, emin, emax, eflux, scale=1.0):
    params = params.copy()
    params[0] = 1.0
    params[0] = eflux / cls.eval_eflux(emin, emax, params, scale=scale)
    return cls(params, scale)