def t0_supconj_to_perpass(t0_supconj, period, ecc, per0):
    return ConstraintParameter(t0_supconj._bundle,
        't0_supconj_to_perpass({}, {}, {}, {})'.format(_get_expr(t0_supconj
        ), _get_expr(period), _get_expr(ecc), _get_expr(per0)))