def pick_monomials_up_to_degree(monomials, degree):
    ordered_monomials = []
    if degree >= 0:
        ordered_monomials.append(S.One)
    for deg in range(1, degree + 1):
        ordered_monomials.extend(pick_monomials_of_degree(monomials, deg))
    return ordered_monomials