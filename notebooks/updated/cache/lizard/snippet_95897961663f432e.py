def read(self, path, wrap_ttl=None):
    path = sanitize_mount(path)
    if path.startswith('cubbyhole'):
        self.token = self.initial_token
        val = super(Client, self).read(path, wrap_ttl)
        self.token = self.operational_token
        return val
    return super(Client, self).read(path, wrap_ttl)