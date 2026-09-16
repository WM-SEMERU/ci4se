def _avro_schema(read_session):
    json_schema = json.loads(read_session.avro_schema.schema)
    column_names = tuple(field['name'] for field in json_schema['fields'])
    return fastavro.parse_schema(json_schema), column_names