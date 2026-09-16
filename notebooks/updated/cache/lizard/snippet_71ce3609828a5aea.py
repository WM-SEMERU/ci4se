def put_auto_follow_pattern(self, name, body, params=None):
    for param in (name, body):
        if param in SKIP_IN_PATH:
            raise ValueError('Empty value passed for a required argument.')
    return self.transport.perform_request('PUT', _make_path('_ccr',
        'auto_follow', name), params=params, body=body)