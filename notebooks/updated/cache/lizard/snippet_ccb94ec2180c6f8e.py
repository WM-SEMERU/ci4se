def validate_api_response(schema, raw_response, request_method='get',
    raw_request=None):
    request = None
    if raw_request is not None:
        request = normalize_request(raw_request)
    response = None
    if raw_response is not None:
        response = normalize_response(raw_response, request=request)
    if response is not None:
        validate_response(response=response, request_method=request_method,
            schema=schema)