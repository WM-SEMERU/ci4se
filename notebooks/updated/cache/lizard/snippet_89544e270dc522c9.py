def xidz(numerator, denominator, value_if_denom_is_zero):
    small = 1e-06
    if abs(denominator) < small:
        return value_if_denom_is_zero
    else:
        return numerator * 1.0 / denominator