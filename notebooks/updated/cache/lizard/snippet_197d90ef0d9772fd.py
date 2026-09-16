def _validate(self, value):
    errors = []
    kwargs = {}
    for validator in self.validators:
        try:
            r = validator(value)
            if not isinstance(validator, Validator) and r is False:
                self.fail('validator_failed')
        except ValidationError as err:
            kwargs.update(err.kwargs)
            if isinstance(err.messages, dict):
                errors.append(err.messages)
            else:
                errors.extend(err.messages)
    if errors:
        raise ValidationError(errors, **kwargs)