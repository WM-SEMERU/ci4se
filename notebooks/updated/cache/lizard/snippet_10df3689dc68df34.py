def remove_access_control_lists(self, security_namespace_id, tokens=None,
    recurse=None):
    route_values = {}
    if security_namespace_id is not None:
        route_values['securityNamespaceId'] = self._serialize.url(
            'security_namespace_id', security_namespace_id, 'str')
    query_parameters = {}
    if tokens is not None:
        query_parameters['tokens'] = self._serialize.query('tokens', tokens,
            'str')
    if recurse is not None:
        query_parameters['recurse'] = self._serialize.query('recurse',
            recurse, 'bool')
    response = self._send(http_method='DELETE', location_id=
        '18a2ad18-7571-46ae-bec7-0c7da1495885', version='5.0', route_values
        =route_values, query_parameters=query_parameters)
    return self._deserialize('bool', response)