def _request(self, url, method='GET', params=None, api_call=None):
    method = method.lower()
    params = params or {}
    func = getattr(requests, method)
    requests_args = {}
    if method == 'get' or method == 'delete':
        requests_args['params'] = params
    else:
        if params.get('json'):
            requests_args['json'] = params.get('json')
        if params.get('files'):
            requests_args['files'] = params.get('files')
        if params.get('data'):
            requests_args['data'] = params.get('data')
    try:
        response = func(url, **requests_args)
    except requests.RequestException as e:
        raise SafecastPyError(str(e))
    if response.status_code > 304:
        if response.status_code == 401:
            raise SafecastPyAuthError(response.json().get('error'))
        if response.status_code in [422]:
            raise SafecastPyError(response.json().get('errors'))
        raise SafecastPyError(response.content, error_code=response.status_code
            )
    try:
        if response.status_code == 204:
            content = response.content
        else:
            content = response.json()
    except ValueError:
        raise SafecastPyError(
            'Response was not valid JSON.                                Unable to decode.'
            )
    return content