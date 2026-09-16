def build_endpoints(conf, endpoint_context, client_authn_method, issuer):
    if issuer.endswith('/'):
        _url = issuer[:-1]
    else:
        _url = issuer
    endpoint = {}
    for name, spec in conf.items():
        try:
            kwargs = spec['kwargs']
        except KeyError:
            kwargs = {}
        if isinstance(spec['class'], str):
            _instance = importer(spec['class'])(endpoint_context=
                endpoint_context, **kwargs)
        else:
            _instance = spec['class'](endpoint_context=endpoint_context, **
                kwargs)
        _instance.endpoint_path = spec['path']
        _instance.full_path = '{}/{}'.format(_url, spec['path'])
        if 'provider_info' in spec:
            _instance.provider_info = spec['provider_info']
        try:
            _client_authn_method = kwargs['client_authn_method']
        except KeyError:
            _instance.client_auth_method = client_authn_method
        else:
            _instance.client_auth_method = _client_authn_method
        endpoint[name] = _instance
    return endpoint