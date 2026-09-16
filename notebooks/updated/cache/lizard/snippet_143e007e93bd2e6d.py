def list_groups(self, scope_ids=None, recurse=None, deleted=None,
    properties=None):
    query_parameters = {}
    if scope_ids is not None:
        query_parameters['scopeIds'] = self._serialize.query('scope_ids',
            scope_ids, 'str')
    if recurse is not None:
        query_parameters['recurse'] = self._serialize.query('recurse',
            recurse, 'bool')
    if deleted is not None:
        query_parameters['deleted'] = self._serialize.query('deleted',
            deleted, 'bool')
    if properties is not None:
        query_parameters['properties'] = self._serialize.query('properties',
            properties, 'str')
    response = self._send(http_method='GET', location_id=
        '5966283b-4196-4d57-9211-1b68f41ec1c2', version='5.0',
        query_parameters=query_parameters)
    return self._deserialize('[Identity]', self._unwrap_collection(response))