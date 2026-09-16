def patch(self, client=None):
    client = self._require_client(client)
    query_params = self._query_params
    query_params['projection'] = 'full'
    update_properties = {key: self._properties[key] for key in self._changes}
    api_response = client._connection.api_request(method='PATCH', path=self
        .path, data=update_properties, query_params=query_params,
        _target_object=self)
    self._set_properties(api_response)