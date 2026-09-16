def search(self, **kwargs):
    return super(ApiInterfaceRequest, self).get(self.prepare_url(
        'api/v3/interface/', kwargs))