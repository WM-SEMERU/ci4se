def validate_int(value):
    if value and not isinstance(value, int):
        try:
            int(str(value))
        except (TypeError, ValueError):
            raise ValidationError('not a valid number')
    return value