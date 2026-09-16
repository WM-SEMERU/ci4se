def get_accounts(self, owner_id=None, member_id=None, properties=None):
    query_parameters = {}
    if owner_id is not None:
        query_parameters['ownerId'] = self._serialize.query('owner_id',
            owner_id, 'str')
    if member_id is not None:
        query_parameters['memberId'] = self._serialize.query('member_id',
            member_id, 'str')
    if properties is not None:
        query_parameters['properties'] = self._serialize.query('properties',
            properties, 'str')
    response = self._send(http_method='GET', location_id=
        '229a6a53-b428-4ffb-a835-e8f36b5b4b1e', version='5.0',
        query_parameters=query_parameters)
    return self._deserialize('[Account]', self._unwrap_collection(response))