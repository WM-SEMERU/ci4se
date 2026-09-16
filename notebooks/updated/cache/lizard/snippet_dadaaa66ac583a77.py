def parse(self, argmap, req=None, locations=None, validate=None,
    error_status_code=None, error_headers=None):
    self.clear_cache()
    req = req if req is not None else self.get_default_request()
    assert req is not None, 'Must pass req object'
    data = None
    validators = _ensure_list_of_callables(validate)
    parser = self._clone()
    schema = self._get_schema(argmap, req)
    try:
        parsed = parser._parse_request(schema=schema, req=req, locations=
            locations or self.locations)
        result = schema.load(parsed)
        data = result.data if MARSHMALLOW_VERSION_INFO[0] < 3 else result
        parser._validate_arguments(data, validators)
    except ma.exceptions.ValidationError as error:
        parser._on_validation_error(error, req, schema, error_status_code,
            error_headers)
    return data