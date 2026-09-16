def parse_endpoint(endpoint, identifier_type=None):
    parts = endpoint.split('.')
    operation = Operation.from_name(parts[1])
    matcher = match(operation.endpoint_pattern, endpoint)
    if not matcher:
        raise InternalServerError('Malformed operation endpoint: {}'.format
            (endpoint))
    kwargs = matcher.groupdict()
    del kwargs['operation']
    if identifier_type is not None:
        kwargs['identifier_type'] = identifier_type
    return operation, Namespace(**kwargs)