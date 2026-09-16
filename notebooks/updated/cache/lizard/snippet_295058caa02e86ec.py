def read_members_of(self, member_id, query_membership=None):
    route_values = {}
    if member_id is not None:
        route_values['memberId'] = self._serialize.url('member_id',
            member_id, 'str')
    query_parameters = {}
    if query_membership is not None:
        query_parameters['queryMembership'] = self._serialize.query(
            'query_membership', query_membership, 'str')
    response = self._send(http_method='GET', location_id=
        '22865b02-9e4a-479e-9e18-e35b8803b8a0', version='5.0-preview.1',
        route_values=route_values, query_parameters=query_parameters)
    return self._deserialize('[str]', self._unwrap_collection(response))