def create_tag(self, name, description=None, servers=[]):
    servers = [str(server) for server in servers]
    body = {'tag': Tag(name, description, servers).to_dict()}
    res = self.request('POST', '/tag', body)
    return Tag(cloud_manager=self, **res['tag'])