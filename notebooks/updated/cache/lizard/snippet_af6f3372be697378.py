def validate(style, value, scalar=False):
    validator = get_validator(style)
    if validator is None:
        return None
    if isinstance(value, (np.ndarray, list)):
        if scalar:
            return False
        return all(validator(v) for v in value)
    return validator(value)