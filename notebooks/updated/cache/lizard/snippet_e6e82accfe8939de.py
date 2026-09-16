def set_python(self, value):
    if not isinstance(value, (list, type(None))):
        raise ValidationError(self.record,
            "Field '{}' must be set to a list, not '{}'".format(self.name,
            value.__class__))
    value = value or []
    self.cursor._validate_list(value)
    return super(ListField, self).set_python(value)