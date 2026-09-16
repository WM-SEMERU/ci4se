def create_domain(self, name):
    args = {'name': name}
    resp = self.request_single('CreateDomain', args)
    return zobjects.Domain.from_dict(resp)