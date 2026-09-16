def patch(self, endpoint, json=None, params=None, **kwargs):
    json = kwargs['data'] if 'data' in kwargs else json
    return self._make_request('patch', endpoint, data=json, params=params)