def _validate_list(self, target):
    min_items = self._field.field_definition.get('minItems')
    max_items = self._field.field_definition.get('maxItems')
    if min_items is not None:
        if len(target) < min_items:
            raise ValidationError(self._record,
                "Field '{}' must have a minimum of {} item(s)".format(self.
                _field.name, min_items))
    if max_items is not None:
        if len(target) > max_items:
            raise ValidationError(self._record,
                "Field '{}' can only have a maximum of {} item(s)".format(
                self._field.name, max_items))
    for item in target:
        self._validate_item(item)