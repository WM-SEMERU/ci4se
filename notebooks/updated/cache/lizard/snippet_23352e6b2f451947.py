def generate_field(name, data):
    assert 'type' in data
    field = TYPES_TO_FIELDS.get(data['type'], Unknown)(name, data)
    return field