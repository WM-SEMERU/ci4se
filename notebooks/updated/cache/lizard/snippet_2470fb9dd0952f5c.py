def create(self, name, numShards, params=None):
    if params is None:
        params = {}
    params.update(name=name, numShards=numShards)
    return self.api('CREATE', params)