def all(self, endpoint, *args, **kwargs):
    kwargs.setdefault('params', {})['offset'] = 0
    kwargs.setdefault('params', {})['limit'] = self.limit
    kwargs['__method__'] = 'get'
    payload = self.request(endpoint, *args, **kwargs)
    has_next = payload.get('result', {}).setdefault('meta', {'next': None})[
        'next']
    while has_next:
        kwargs['params']['offset'] += self.limit
        _payload = self.request(endpoint, *args, **kwargs)
        payload['result']['data'].extend(_payload['result']['data'])
        has_next = _payload['result']['meta']['next']
    del payload['result']['meta']
    return payload