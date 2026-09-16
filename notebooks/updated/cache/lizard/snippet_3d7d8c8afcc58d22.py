def update(self, fields=None, **kwargs):
    kwargs = kwargs.copy()
    kwargs.update(self._server_config.get_client_kwargs())
    headers = kwargs.pop('headers', {})
    headers['content-type'] = 'multipart/form-data'
    kwargs['headers'] = headers
    return client.put(self.path('self'), fields, **kwargs)