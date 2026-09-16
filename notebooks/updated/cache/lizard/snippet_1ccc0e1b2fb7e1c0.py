def get_user(self, username=None, params=None):
    return self.transport.perform_request('GET', _make_path('_security',
        'user', username), params=params)