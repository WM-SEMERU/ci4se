def expect_request(self, schema, merge=False):
    schema = self._input_object(schema)
    if 'properties' not in schema:
        schema = {'properties': schema}
    if self._input_boolean(merge):
        new_schema = SchemaBuilder(schema_uri=False)
        new_schema.add_schema(self.schema['properties']['request'])
        new_schema.add_schema(schema)
        self.schema['properties']['request'] = new_schema.to_schema()
    else:
        self.schema['properties']['request'] = schema
    return self.schema['properties']['request']