def get_service_definitions(self, service_type=None):
    route_values = {}
    if service_type is not None:
        route_values['serviceType'] = self._serialize.url('service_type',
            service_type, 'str')
    response = self._send(http_method='GET', location_id=
        'd810a47d-f4f4-4a62-a03f-fa1860585c4c', version='5.0-preview.1',
        route_values=route_values)
    return self._deserialize('[ServiceDefinition]', self._unwrap_collection
        (response))