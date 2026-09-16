def _get_request_body(request_body):
    if request_body is None:
        return b''
    if isinstance(request_body, bytes) or isinstance(request_body, IOBase):
        return request_body
    if isinstance(request_body, _unicode_type):
        return request_body.encode('utf-8')
    request_body = str(request_body)
    if isinstance(request_body, _unicode_type):
        return request_body.encode('utf-8')
    return request_body