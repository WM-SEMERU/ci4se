def schema_map(schema):
    mapper = {}
    for name in getFieldNames(schema):
        mapper[name] = name
    return mapper