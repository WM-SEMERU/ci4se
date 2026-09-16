def list(self, params=None):
    params = params if params else dict()
    return self.request('/v1/sshkey/list', params, 'GET')