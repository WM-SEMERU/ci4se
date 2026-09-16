def _insert_entity(entity):
    _validate_entity(entity)
    request = HTTPRequest()
    request.method = 'POST'
    request.headers = [_DEFAULT_CONTENT_TYPE_HEADER, _DEFAULT_PREFER_HEADER,
        _DEFAULT_ACCEPT_HEADER]
    request.body = _get_request_body(_convert_entity_to_json(entity))
    return request