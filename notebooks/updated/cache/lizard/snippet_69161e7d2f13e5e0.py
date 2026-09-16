def validate_api_call(schema, raw_request, raw_response):
    request = normalize_request(raw_request)
    with ErrorDict() as errors:
        try:
            validate_request(request=request, schema=schema)
        except ValidationError as err:
            errors['request'].add_error(err.messages or getattr(err, 'detail'))
            return
        response = normalize_response(raw_response, raw_request)
        try:
            validate_response(response=response, request_method=request.
                method, schema=schema)
        except ValidationError as err:
            errors['response'].add_error(err.messages or getattr(err, 'detail')
                )