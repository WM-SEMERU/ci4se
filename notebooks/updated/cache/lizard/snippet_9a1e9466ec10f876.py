def to_match(self):
    self.validate()
    mark_name, field_name = self.location.get_location_name()
    validate_safe_string(mark_name)
    if field_name is None:
        return '$matched.%s' % (mark_name,)
    else:
        validate_safe_string(field_name)
        return '$matched.%s.%s' % (mark_name, field_name)