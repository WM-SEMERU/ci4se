def get_schema(self, schema_id):
    schema_specs = get_schema_specs(schema_id, self)
    if schema_specs is None:
        raise KeyError("Specified schema_id '{0}' not found".format(schema_id))
    for schema in (parameter.get('schema') for parameter in schema_specs[
        'parameters']):
        if schema is not None and schema.get('id').lower() == schema_id:
            return schema