def coefficients_non_uni(deriv, acc, coords, idx):
    if acc % 2 == 1:
        acc += 1
    num_central = 2 * math.floor((deriv + 1) / 2) - 1 + acc
    num_side = num_central // 2
    if deriv % 2 == 0:
        num_coef = num_central + 1
    else:
        num_coef = num_central
    if idx < num_side:
        matrix = _build_matrix_non_uniform(0, num_coef - 1, coords, idx)
        rhs = _build_rhs(0, num_coef - 1, deriv)
        ret = {'coefficients': np.linalg.solve(matrix, rhs), 'offsets': np.
            array([p for p in range(num_coef)])}
    elif idx >= len(coords) - num_side:
        matrix = _build_matrix_non_uniform(num_coef - 1, 0, coords, idx)
        rhs = _build_rhs(num_coef - 1, 0, deriv)
        ret = {'coefficients': np.linalg.solve(matrix, rhs), 'offsets': np.
            array([p for p in range(-num_coef + 1, 1)])}
    else:
        matrix = _build_matrix_non_uniform(num_side, num_side, coords, idx)
        rhs = _build_rhs(num_side, num_side, deriv)
        ret = {'coefficients': np.linalg.solve(matrix, rhs), 'offsets': np.
            array([p for p in range(-num_side, num_side + 1)])}
    return ret