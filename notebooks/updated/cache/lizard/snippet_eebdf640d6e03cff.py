def _sin_to_angle(result, deriv, side=1):
    v = np.arcsin(np.clip(result[0], -1, 1))
    sign = side
    if sign == -1:
        if v < 0:
            offset = -np.pi
        else:
            offset = np.pi
    else:
        offset = 0.0
    if deriv == 0:
        return v * sign + offset,
    if abs(result[0]) >= 1:
        factor1 = 0
    else:
        factor1 = 1.0 / np.sqrt(1 - result[0] ** 2)
    d = factor1 * result[1]
    if deriv == 1:
        return v * sign + offset, d * sign
    factor2 = result[0] * factor1 ** 3
    dd = factor2 * np.outer(result[1], result[1]) + factor1 * result[2]
    if deriv == 2:
        return v * sign + offset, d * sign, dd * sign
    raise ValueError('deriv must be 0, 1 or 2.')