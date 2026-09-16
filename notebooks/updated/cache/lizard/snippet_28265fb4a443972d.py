def add_definitions(definitions, operations):
    for definition_schema in iter_definitions(definitions, operations):
        if definition_schema is None:
            continue
        if isinstance(definition_schema, str):
            continue
        for name, schema in iter_schemas(definition_schema):
            definitions.setdefault(name, swagger.Schema(schema))