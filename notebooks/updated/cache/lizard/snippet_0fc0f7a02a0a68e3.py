def get_feature_flag_by_name(self, name, check_feature_exists=None):
    route_values = {}
    if name is not None:
        route_values['name'] = self._serialize.url('name', name, 'str')
    query_parameters = {}
    if check_feature_exists is not None:
        query_parameters['checkFeatureExists'] = self._serialize.query(
            'check_feature_exists', check_feature_exists, 'bool')
    response = self._send(http_method='GET', location_id=
        '3e2b80f8-9e6f-441e-8393-005610692d9c', version='5.0-preview.1',
        route_values=route_values, query_parameters=query_parameters)
    return self._deserialize('FeatureFlag', response)