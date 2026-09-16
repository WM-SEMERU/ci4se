def accept(self, value, silent=False):
    try:
        value = self.to_python(value)
        for v in self.validators:
            value = v(self, value)
        if self.required and self._is_empty(value):
            raise ValidationError(self.error_required)
    except ValidationError as e:
        if not silent:
            e.fill_errors(self.field)
        value = self._existing_value
    return value