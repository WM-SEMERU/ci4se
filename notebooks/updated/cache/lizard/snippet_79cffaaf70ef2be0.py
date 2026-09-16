def verify_create(self, recipient, params=None):
    if params is None:
        params = {}
    params.update({'recipient': recipient})
    return Verify().load(self.request('verify', 'POST', params))