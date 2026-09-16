def get_prep_value(self, value):
    if value is None or value == '':
        return None
    if isinstance(value, six.string_types):
        value = _hex_string_to_unsigned_integer(value)
    if _using_signed_storage():
        value = _unsigned_to_signed_integer(value)
    return value