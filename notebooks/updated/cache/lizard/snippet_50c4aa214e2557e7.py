def available_repositories(self, **kwargs):
    if 'data' not in kwargs:
        kwargs['data'] = dict()
        kwargs['data']['product_id'] = self.product.id
    kwargs = kwargs.copy()
    kwargs.update(self._server_config.get_client_kwargs())
    response = client.get(self.path('available_repositories'), **kwargs)
    return _handle_response(response, self._server_config)