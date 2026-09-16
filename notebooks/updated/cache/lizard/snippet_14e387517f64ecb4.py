def _requests(self, url, method='GET', headers=None, params=None, data=None,
    errors=None):
    title = '%s._requests' % self.__class__.__name__
    from time import time
    import requests
    if not self._access_token:
        self.access_token()
        if self.retrieve_details:
            self._get_products()
    current_time = time()
    if current_time > self.expires_at:
        self.access_token()
        if self.retrieve_details:
            self._get_products()
    request_kwargs = {'url': url, 'headers': {'Authorization': 'Bearer %s' %
        self._access_token, 'Accept': 'application/json;v=2'}, 'params': {},
        'data': {}}
    if headers:
        request_kwargs['headers'].update(headers)
    if params:
        request_kwargs['params'].update(params)
    if data:
        request_kwargs['data'].update(data)
    if method == 'POST':
        try:
            response = requests.post(**request_kwargs)
        except Exception:
            if self.requests_handler:
                request_kwargs['method'] = 'POST'
                request_object = requests.Request(**request_kwargs)
                return self.requests_handler(request_object)
            else:
                raise
    elif method == 'GET':
        try:
            response = requests.get(**request_kwargs)
        except Exception:
            if self.requests_handler:
                request_kwargs['method'] = 'GET'
                request_object = requests.Request(**request_kwargs)
                return self.requests_handler(request_object)
            else:
                raise
    else:
        raise ValueError('%s(method=) must be either GET or POST' % title)
    response_details = self.response_handler.handle(response, errors)
    return response_details