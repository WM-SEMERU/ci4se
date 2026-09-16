def run_validation(self, data=empty):
    is_empty_value, data = self.validate_empty_values(data)
    if is_empty_value:
        return data
    value = self.to_internal_value(data)
    try:
        self.run_validators(value)
        value = self.validate(value)
        assert value is not None, '.validate() should return the validated data'
    except (ValidationError, DjangoValidationError) as exc:
        raise ValidationError(detail=get_validation_error_detail(exc))
    return value