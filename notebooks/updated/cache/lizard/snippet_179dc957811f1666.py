def put_script(self, id, body, context=None, params=None):
    for param in (id, body):
        if param in SKIP_IN_PATH:
            raise ValueError('Empty value passed for a required argument.')
    return self.transport.perform_request('PUT', _make_path('_scripts', id,
        context), params=params, body=body)