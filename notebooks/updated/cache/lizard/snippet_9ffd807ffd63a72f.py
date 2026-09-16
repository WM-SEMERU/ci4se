def _to_power_basis_degree8(nodes1, nodes2):
    r
    evaluated = [eval_intersection_polynomial(nodes1, nodes2, t_val) for
        t_val in _CHEB9]
    return polynomial.polyfit(_CHEB9, evaluated, 8)