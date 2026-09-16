def schema2parameters(self, schema, default_in='body', name='body',
    required=False, description=None):
    openapi_default_in = __location_map__.get(default_in, default_in)
    if self.openapi_version.major < 3 and openapi_default_in == 'body':
        prop = self.resolve_schema_dict(schema)
        param = {'in': openapi_default_in, 'required': required, 'name':
            name, 'schema': prop}
        if description:
            param['description'] = description
        return [param]
    assert not getattr(schema, 'many', False
        ), "Schemas with many=True are only supported for 'json' location (aka 'in: body')"
    fields = get_fields(schema, exclude_dump_only=True)
    return self.fields2parameters(fields, default_in=default_in)