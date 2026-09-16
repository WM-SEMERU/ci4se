def construct(self, request, service=None, http_args=None, **kwargs):
    if http_args is None:
        http_args = {}
    if 'headers' not in http_args:
        http_args['headers'] = {}
    try:
        passwd = kwargs['password']
    except KeyError:
        try:
            passwd = request['client_secret']
        except KeyError:
            passwd = service.service_context.client_secret
    try:
        user = kwargs['user']
    except KeyError:
        user = service.service_context.client_id
    credentials = '{}:{}'.format(quote_plus(user), quote_plus(passwd))
    authz = base64.urlsafe_b64encode(credentials.encode('utf-8')).decode(
        'utf-8')
    http_args['headers']['Authorization'] = 'Basic {}'.format(authz)
    try:
        del request['client_secret']
    except (KeyError, TypeError):
        pass
    if isinstance(request, AccessTokenRequest) and request['grant_type'
        ] == 'authorization_code':
        if 'client_id' not in request:
            try:
                request['client_id'] = service.service_context.client_id
            except AttributeError:
                pass
    else:
        try:
            _req = request.c_param['client_id'][VREQUIRED]
        except (KeyError, AttributeError):
            _req = False
        if not _req:
            try:
                del request['client_id']
            except KeyError:
                pass
    return http_args