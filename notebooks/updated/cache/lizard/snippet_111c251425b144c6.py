def get_value_from_schema(schema, definition: dict, key: str,
    definition_key: str):
    resolved_definition = definition.copy()
    if '$ref' in resolved_definition:
        try:
            resolved_definition = schema.resolve(definition['$ref'])
        except SchemaError as e:
            raise TypeSystemError(str(e))
    try:
        value = resolved_definition[key]
    except KeyError:
        if resolved_definition['type'] == 'array':
            return [get_value_from_schema(schema, resolved_definition[
                'items'], key, definition_key)]
        elif resolved_definition['type'] == 'object':
            value = {}
            for prop, definition in resolved_definition['properties'].items():
                value[prop] = get_value_from_schema(schema, definition, key,
                    definition_key)
            return value
        raise TypeSystemError('Definition `{}` is missing a {}.'.format(
            definition_key, key))
    return value