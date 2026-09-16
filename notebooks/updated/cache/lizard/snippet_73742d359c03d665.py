def validate_element(self, value):
    if isinstance(value, bytes):
        try:
            six.text_type(value, 'UTF-8')
        except UnicodeDecodeError as err:
            try:
                _ = self.name
            except AttributeError:
                validation_error = ValidationError(
                    'Field encountered non-UTF-8 string %r: %s' % (value, err))
            else:
                validation_error = ValidationError(
                    'Field %s encountered non-UTF-8 string %r: %s' % (self.
                    name, value, err))
                validation_error.field_name = self.name
            raise validation_error
    else:
        return super(StringField, self).validate_element(value)
    return value