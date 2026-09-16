def validate(data, schema=None):
    schema = _load_schema_for_record(data, schema)
    return jsonschema_validate(instance=data, schema=schema, resolver=
        LocalRefResolver.from_schema(schema), format_checker=
        inspire_format_checker)