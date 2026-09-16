def _cos_to_angle(result, deriv, sign=1):
    v = np.arccos(np.clip(result[0], -1, 1))
    if deriv == 0:
        return v * sign,
    if abs(result[0]) >= 1:
        factor1 = 0
    else:
        factor1 = -1.0 / np.sqrt(1 - result[0] ** 2)
    d = factor1 * result[1]
    if deriv == 1:
        return v * sign, d * sign
    factor2 = result[0] * factor1 ** 3
    dd = factor2 * np.outer(result[1], result[1]) + factor1 * result[2]
    if deriv == 2:
        return v * sign, d * sign, dd * sign
    raise ValueError('deriv must be 0, 1 or 2.')