def make_request(request, method, default_headers=None, **kwargs):
    kwargs = convert(kwargs)
    if not default_headers:
        headers = dict(DEFAULT_HEADERS)
    else:
        headers = default_headers.copy()
    if isinstance(request, HTTPRequest):
        headers.update(request.headers)
    if 'headers' in kwargs:
        headers.update(kwargs.pop('headers'))
    if isinstance(request, HTTPRequest):
        request.method = method
        request.headers.update(headers)
    else:
        request = HTTPRequest(request, method, headers)
    if kwargs:
        if method in ['GET', 'DELETE']:
            request.url = '{}?{}'.format(request.url, urllib.urlencode(kwargs))
        elif method in ['POST', 'PUT']:
            if request.headers['Content-Type'] == JSON_TYPE:
                request.body = json.dumps(kwargs)
            elif 'body' in kwargs:
                request.body = kwargs['body']
    return request