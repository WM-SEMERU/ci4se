def get_nested_fields(schema, model_field=False):
    nested_fields = []
    for key, value in schema._declared_fields.items():
        if isinstance(value, List) and isinstance(value.container, Nested):
            nested_fields.append(key)
        elif isinstance(value, Nested):
            nested_fields.append(key)
    if model_field is True:
        nested_fields = [get_model_field(schema, key) for key in nested_fields]
    return nested_fields