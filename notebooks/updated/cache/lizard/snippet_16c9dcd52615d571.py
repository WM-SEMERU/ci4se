def _validate_schema(schema, body):
    try:
        schema[1](rapidjson.dumps(body))
    except ValueError as exc:
        try:
            jsonschema.validate(body, schema[0])
        except jsonschema.ValidationError as exc2:
            raise SchemaValidationError(str(exc2)) from exc2
        logger.warning(
            'code problem: jsonschema did not raise an exception, wheras rapidjson raised %s'
            , exc)
        raise SchemaValidationError(str(exc)) from exc