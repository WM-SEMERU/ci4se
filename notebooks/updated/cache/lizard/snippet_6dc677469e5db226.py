def _parse_lambda_output(lambda_output, binary_types, flask_request):
    json_output = json.loads(lambda_output)
    if not isinstance(json_output, dict):
        raise TypeError('Lambda returned %{s} instead of dict', type(
            json_output))
    status_code = json_output.get('statusCode') or 200
    headers = CaseInsensitiveDict(json_output.get('headers') or {})
    body = json_output.get('body') or 'no data'
    is_base_64_encoded = json_output.get('isBase64Encoded') or False
    try:
        status_code = int(status_code)
        if status_code <= 0:
            raise ValueError
    except ValueError:
        message = 'statusCode must be a positive int'
        LOG.error(message)
        raise TypeError(message)
    if 'Content-Type' not in headers:
        LOG.info("No Content-Type given. Defaulting to 'application/json'.")
        headers['Content-Type'] = 'application/json'
    if LocalApigwService._should_base64_decode_body(binary_types,
        flask_request, headers, is_base_64_encoded):
        body = base64.b64decode(body)
    return status_code, headers, body