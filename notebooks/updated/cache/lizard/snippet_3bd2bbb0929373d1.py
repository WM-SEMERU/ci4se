def get_connected_service_details(self, project_id, name):
    route_values = {}
    if project_id is not None:
        route_values['projectId'] = self._serialize.url('project_id',
            project_id, 'str')
    if name is not None:
        route_values['name'] = self._serialize.url('name', name, 'str')
    response = self._send(http_method='GET', location_id=
        'b4f70219-e18b-42c5-abe3-98b07d35525e', version='5.0-preview.1',
        route_values=route_values)
    return self._deserialize('WebApiConnectedServiceDetails', response)