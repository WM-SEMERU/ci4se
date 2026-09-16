def render_descriptor(data):
    if not data.descriptor_schema:
        return
    for field_schema, field, path in iterate_schema(data.descriptor, data.
        descriptor_schema.schema, 'descriptor'):
        if 'default' in field_schema and field_schema['name'] not in field:
            dict_dot(data, path, field_schema['default'])