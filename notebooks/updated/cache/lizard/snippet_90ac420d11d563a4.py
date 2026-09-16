def validate_type_only(self, val):
    if not isinstance(val, self.definition):
        raise ValidationError('expected type %s, got %s' % (self.definition
            .__name__, generic_type_name(val)))