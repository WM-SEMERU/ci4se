def _validate_input_data(self, data, request):
    validator = self._get_input_validator(request)
    if isinstance(data, (list, tuple)):
        return map(validator.validate, data)
    else:
        return validator.validate(data)