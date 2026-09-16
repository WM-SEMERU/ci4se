def load_schema(schema_path):
    with open(schema_path, 'r') as schema_file:
        schema = simplejson.load(schema_file)
    resolver = RefResolver('', '', schema.get('models', {}))
    return build_request_to_validator_map(schema, resolver)