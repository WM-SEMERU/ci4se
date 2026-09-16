def esinw2per0(ecc, esinw):
    return ConstraintParameter(ecc._bundle, 'esinw2per0({}, {})'.format(
        _get_expr(ecc), _get_expr(esinw)))