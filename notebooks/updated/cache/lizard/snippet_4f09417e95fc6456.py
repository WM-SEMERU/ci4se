def access_token(self):
    title = '%s.access_token' % self.__class__.__name__
    from time import time
    import requests
    request_kwargs = {'url': self.token_endpoint, 'data': {'client_id':
        self.client_id, 'client_secret': self.client_secret, 'grant_type':
        'client_credentials'}}
    try:
        current_time = time()
        response = requests.post(**request_kwargs)
    except Exception:
        if self.requests_handler:
            request_kwargs['method'] = 'POST'
            request_object = requests.Request(**request_kwargs)
            return self.requests_handler(request_object)
        else:
            raise
    response_details = self.response_handler.handle(response)
    if response_details['json']:
        self._access_token = response_details['json']['access_token']
        expires_in = response_details['json']['expires_in']
        self.expires_at = current_time + expires_in
    return self._access_token