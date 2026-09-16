def encode_as_simple(name, value):
    if isinstance(value, objectify.ObjectifiedDataElement):
        return encode_as_simple(name, unicode(value))
    if type(value) in _stringable_types:
        value = str(value)
    return elements.field(name, value)