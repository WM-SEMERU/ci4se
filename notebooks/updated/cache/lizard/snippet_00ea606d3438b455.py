def _compute_valid(self):
    r
    if self._dimension != 2:
        raise NotImplementedError('Validity check only implemented in R^2')
    poly_sign = None
    if self._degree == 1:
        first_deriv = self._nodes[:, 1:] - self._nodes[:, :-1]
        poly_sign = _SIGN(np.linalg.det(first_deriv))
    elif self._degree == 2:
        bernstein = _surface_helpers.quadratic_jacobian_polynomial(self._nodes)
        poly_sign = _surface_helpers.polynomial_sign(bernstein, 2)
    elif self._degree == 3:
        bernstein = _surface_helpers.cubic_jacobian_polynomial(self._nodes)
        poly_sign = _surface_helpers.polynomial_sign(bernstein, 4)
    else:
        raise _helpers.UnsupportedDegree(self._degree, supported=(1, 2, 3))
    return poly_sign == 1