def content_create(self, params):
    r = self.request(method='content.create', data=params)
    return self._handle_error(r, 'Could not create object {}.'.format(repr(
        params)))