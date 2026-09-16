def _wrap_class(request_handler, validator):
    METHODS = ['get', 'post', 'put', 'head', 'options', 'delete', 'patch']
    for name in METHODS:
        method = getattr(request_handler, name)
        setattr(request_handler, name, _auth_required(method, validator))
    return request_handler