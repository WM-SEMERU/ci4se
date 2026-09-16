def _to_power_basis23(nodes1, nodes2):
    r
    evaluated = [eval_intersection_polynomial(nodes1, nodes2, t_val) for
        t_val in _CHEB7]
    return polynomial.polyfit(_CHEB7, evaluated, 6)