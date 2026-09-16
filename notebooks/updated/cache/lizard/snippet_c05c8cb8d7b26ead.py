def reload(self, client=None):
    client = self._require_client(client)
    query_params = self._query_params
    query_params['projection'] = 'noAcl'
    api_response = client._connection.api_request(method='GET', path=self.
        path, query_params=query_params, headers=self._encryption_headers(),
        _target_object=self)
    self._set_properties(api_response)