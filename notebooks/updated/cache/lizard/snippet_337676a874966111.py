def create_expansions(self, environment_id, collection_id, expansions, **kwargs
    ):
    if environment_id is None:
        raise ValueError('environment_id must be provided')
    if collection_id is None:
        raise ValueError('collection_id must be provided')
    if expansions is None:
        raise ValueError('expansions must be provided')
    expansions = [self._convert_model(x, Expansion) for x in expansions]
    headers = {}
    if 'headers' in kwargs:
        headers.update(kwargs.get('headers'))
    sdk_headers = get_sdk_headers('discovery', 'V1', 'create_expansions')
    headers.update(sdk_headers)
    params = {'version': self.version}
    data = {'expansions': expansions}
    url = '/v1/environments/{0}/collections/{1}/expansions'.format(*self.
        _encode_path_vars(environment_id, collection_id))
    response = self.request(method='POST', url=url, headers=headers, params
        =params, json=data, accept_json=True)
    return response