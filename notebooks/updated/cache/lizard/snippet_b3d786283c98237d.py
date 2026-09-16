def any(*validators):

    def validate_any(fields):
        errors = {}
        for validator in validators:
            validation_errors = validator(fields)
            if not validation_errors:
                return
            errors.update(validation_errors)
        return errors
    validate_any.__doc__ = ' or '.join(validator.__doc__ for validator in
        validators)
    return validate_any