def esinw(b, orbit, solve_for=None, **kwargs):
    orbit_ps = _get_system_ps(b, orbit)
    metawargs = orbit_ps.meta
    metawargs.pop('qualifier')
    esinw_def = FloatParameter(qualifier='esinw', value=0.0, default_unit=u
        .dimensionless_unscaled, limits=(-1.0, 1.0), description=
        'Eccentricity times sin of argument of periastron')
    esinw, created = b.get_or_create('esinw', esinw_def, **metawargs)
    ecc = b.get_parameter(qualifier='ecc', **metawargs)
    per0 = b.get_parameter(qualifier='per0', **metawargs)
    if solve_for in [None, esinw]:
        lhs = esinw
        rhs = ecc * sin(per0)
    elif solve_for == ecc:
        lhs = ecc
        rhs = esinw / sin(per0)
    elif solve_for == per0:
        lhs = per0
        rhs = esinw2per0(ecc, esinw)
    else:
        raise NotImplementedError
    return lhs, rhs, {'orbit': orbit}