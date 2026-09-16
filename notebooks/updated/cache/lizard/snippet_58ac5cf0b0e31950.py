def convert_row(self, keyed_row, schema, fallbacks):
    for key, value in list(keyed_row.items()):
        field = schema.get_field(key)
        if not field:
            del keyed_row[key]
        if key in fallbacks:
            value = _uncast_value(value, field=field)
        else:
            value = field.cast_value(value)
        keyed_row[key] = value
    return keyed_row