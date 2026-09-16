def disable_validation(self, field_name):
    field = self.field_dict.get(field_name)
    if not field:
        raise exceptions.FieldNotFound(
            "Field not found: '%s' when trying to disable validation" %
            field_name)
    field.validators = []