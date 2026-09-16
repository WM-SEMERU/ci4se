def construct(self, request, service=None, http_args=None, **kwargs):
    _acc_token = ''
    for _token_type in ['access_token', 'refresh_token']:
        _acc_token = find_token(request, _token_type, service, **kwargs)
        if _acc_token:
            break
    if not _acc_token:
        raise KeyError('No access or refresh token available')
    else:
        request['access_token'] = _acc_token
    return http_args