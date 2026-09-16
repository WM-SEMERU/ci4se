def _get_msge_with_gradient_func(shape, p):
    t, m, l = shape
    n = (l - p) * t
    underdetermined = n < m * p
    if underdetermined:
        return _msge_with_gradient_underdetermined
    else:
        return _msge_with_gradient_overdetermined