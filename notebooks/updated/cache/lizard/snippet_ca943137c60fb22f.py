def patch(self, service, path, body, **kwargs):
    return self.make_request(Methods.PATCH, service, path, body=body, **kwargs)