def _get_sigma_coeffs(coeffs):
    r
    num_nodes, = coeffs.shape
    degree = num_nodes - 1
    effective_degree = None
    for index in six.moves.range(degree, -1, -1):
        if coeffs[index] != 0.0:
            effective_degree = index
            break
    if effective_degree is None:
        return None, 0, 0
    if effective_degree == 0:
        return None, degree, 0
    sigma_coeffs = coeffs[:effective_degree] / coeffs[effective_degree]
    binom_numerator = effective_degree
    binom_denominator = degree - effective_degree + 1
    for exponent in six.moves.xrange(effective_degree - 1, -1, -1):
        sigma_coeffs[exponent] *= binom_numerator
        sigma_coeffs[exponent] /= binom_denominator
        binom_numerator *= exponent
        binom_denominator *= degree - exponent + 1
    return sigma_coeffs, degree, effective_degree