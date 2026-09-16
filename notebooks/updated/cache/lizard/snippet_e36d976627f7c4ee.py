def query_security_namespaces(self, security_namespace_id=None, local_only=None
    ):
    route_values = {}
    if security_namespace_id is not None:
        route_values['securityNamespaceId'] = self._serialize.url(
            'security_namespace_id', security_namespace_id, 'str')
    query_parameters = {}
    if local_only is not None:
        query_parameters['localOnly'] = self._serialize.query('local_only',
            local_only, 'bool')
    response = self._send(http_method='GET', location_id=
        'ce7b9f95-fde9-4be8-a86d-83b366f0b87a', version='5.0', route_values
        =route_values, query_parameters=query_parameters)
    return self._deserialize('[SecurityNamespaceDescription]', self.
        _unwrap_collection(response))