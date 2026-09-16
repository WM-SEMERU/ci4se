def min_validator(min_value):

    def validator(value):
        if value < min_value:
            raise ValidationError('{} is not >= {}'.format(value, min_value))
    return validator