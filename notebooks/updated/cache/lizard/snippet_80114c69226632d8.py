def _normalize(schema, allow_none=True):
    if allow_none and schema is None:
        return schema
    if isinstance(schema, CommonSchema):
        return schema
    if isinstance(schema, StreamSchema):
        return schema
    if isinstance(schema, basestring):
        return StreamSchema(schema)
    py_types = {_spl_object: CommonSchema.Python, _spl_str: CommonSchema.
        String, json: CommonSchema.Json}
    if schema in py_types:
        return py_types[schema]
    if sys.version_info.major == 3:
        import typing
        if isinstance(schema, type) and issubclass(schema, tuple):
            if hasattr(schema, '_fields') and hasattr(schema, '_field_types'):
                return _from_named_tuple(schema)
    raise ValueError('Unknown stream schema type:' + str(schema))