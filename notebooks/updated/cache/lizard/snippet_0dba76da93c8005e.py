def is_finite_number(value):
    if not isinstance(value, (numbers.Integral, float)):
        return False
    if isinstance(value, bool):
        return False
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return False
    if abs(value) > 2 ** 53:
        return False
    return True