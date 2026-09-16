def delete_service_endpoint(self, project, endpoint_id, deep=None):
    route_values = {}
    if project is not None:
        route_values['project'] = self._serialize.url('project', project, 'str'
            )
    if endpoint_id is not None:
        route_values['endpointId'] = self._serialize.url('endpoint_id',
            endpoint_id, 'str')
    query_parameters = {}
    if deep is not None:
        query_parameters['deep'] = self._serialize.query('deep', deep, 'bool')
    self._send(http_method='DELETE', location_id=
        'e85f1c62-adfc-4b74-b618-11a150fb195e', version='5.0-preview.2',
        route_values=route_values, query_parameters=query_parameters)